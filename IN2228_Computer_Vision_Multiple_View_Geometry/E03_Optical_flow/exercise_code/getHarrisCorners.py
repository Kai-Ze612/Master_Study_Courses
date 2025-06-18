import numpy as np

def getHarrisCorners(M, kappa, theta):
    """
    Compute Harris corners using the structure tensor (simplified version)
    """
    # Extract elements of structure tensor
    M11 = M[:, :, 0, 0]  # Ix^2
    M12 = M[:, :, 0, 1]  # Ix*Iy
    M22 = M[:, :, 1, 1]  # Iy^2
    
    # Compute determinant and trace
    det_M = M11 * M22 - M12 * M12
    trace_M = M11 + M22
    
    # Harris corner response
    score = det_M - kappa * (trace_M ** 2)
    
    # Apply threshold
    corner_candidates = score > theta
    
    # Simplified non-maximum suppression
    H, W = score.shape
    local_maxima = np.zeros_like(score, dtype=bool)
    
    for i in range(H):
        for j in range(W):
            if not corner_candidates[i, j]:
                continue
                
            # Check 3x3 neighborhood
            is_local_max = True
            for di in [-1, 0, 1]:
                for dj in [-1, 0, 1]:
                    ni, nj = i + di, j + dj
                    # Skip center pixel and out-of-bounds
                    if (di == 0 and dj == 0) or ni < 0 or ni >= H or nj < 0 or nj >= W:
                        continue
                    # If any neighbor has higher score, not a local maximum
                    if score[ni, nj] > score[i, j]:
                        is_local_max = False
                        break
                if not is_local_max:
                    break
            
            local_maxima[i, j] = is_local_max
    
    # Final corners
    corners = corner_candidates & local_maxima
    
    # Extract coordinates
    corner_indices = np.where(corners)
    points = np.column_stack((corner_indices[1], corner_indices[0]))
   
    return score, points