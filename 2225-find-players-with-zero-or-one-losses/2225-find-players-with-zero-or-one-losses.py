class Solution:
    def findWinners(self, matches: list[list[int]]) -> list[list[int]]:
        losses = defaultdict(int)

        for winner, loser in matches:
            if winner not in losses:
                losses[winner] = 0
            if loser not in losses:
                losses[loser] = 0
            losses[loser] += 1
        
        zero_losses = []
        one_loss = []

        for player in losses:
            if losses[player] == 0:
                zero_losses.append(player)
            elif losses[player] == 1:
                one_loss.append(player)

        zero_losses.sort()
        one_loss.sort()
        return [zero_losses, one_loss]
            


                


