p <- ggplot(
  ChickWeight, 
  aes(x = weight, y=Chick, size = weight, colour = Diet)
  ) +
  geom_point(show.legend = FALSE, alpha = 0.7) +
  scale_color_viridis_d() +
  scale_size(range = c(2, 12)) +
  scale_x_log10() +
  labs(x = "Weight", y = "Chick")
  
p + transition_time(Time) + labs(title = "Day: {frame_time}")