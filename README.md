# Bass Diffusion Model Implementation

## Overview
This project implements the **Bass Diffusion Model**, which estimates the adoption of an innovation over time using innovation and imitation parameters.

---

# Innovation Diffusion Analysis Based on TIME’s Best Innovations List

## Choosing an Innovation from the List
I chose **[An Artistic E-Reader](https://time.com/7094611/rakuten-kobo-libra-colour/)** from TIME's Best Innovations.

## Identifing a Similar Innovation from the Past
A perfect example would be **[Amazon Kindle Paperwhite](https://press.aboutamazon.com/2012/9/introducing-the-new-kindle-paperwhite-the-most-advanced-e-reader-ever-constructed/)**, introduced in 2012. The Kindle Paperwhite offers a high-resolution display and built-in front light for a comfortable, paper-like reading experience. Additonally, It allowea users to browse, purchase, download, and read digital content like e-books, newspapers, and magazines.

The **[Kobo Libra Colour](https://www.theverge.com/2024/11/27/24307532/black-friday-best-deal-e-reader-kobo-libra-colour-cyber-monday)** builds upon this foundation by incorporating E Ink Kaleido 3 technology, enabling color display while maintaining the eye-friendly and battery-efficient qualities of traditional e-readers. This advancement allows for a more vibrant presentation of content such as comic books, magazines, and illustrated materials, which were not good displayed on original Kindle Paperwhite because of its monochrome display. Additionally, the Libra Colour offers features like physical page-turn buttons and note-taking, enhancing user interaction and functionality.

Both devices prioritize portability and user comfort, but the **Kobo Libra Colour** expands the e-reading experience with **color and interactive capabilities**.

## Choosing a scope (global or country-specific).

Here I analyze the diffusion of the product within the United States, as my dataset is based on US e-book sales. The US is one of the largest markets for e-readers, with widespread digital book adoption driven by companies like Amazon and Rakuten Kobo (Statista, 2024). Focusing on the US ensures more accurate modeling and aligns with available consumer behavior data.


---

## Model Formula
The adoption fraction \( F(t) \) is calculated using:
[F_t = F_{t-1} + (p + q * F_{t-1}) * (1 - F_{t-1})]

The number of new adopters \( S(t) \):
[S_t = M *  (F_t - F_{t-1})]

where:
- **M** = Market size (total adopters)
- **p** = Coefficient of innovation
- **q** = Coefficient of imitation
- **F_t** = Cumulative fraction of adopters at time t
- **S_t** = Number of new adopters at time t


## Visualization
The model includes visualizations such as:
- A line plot showing cumulative adoption over time.
- A bar chart displaying the number of new adopters per period.
- Difussion model fit

## References  

- Amazon Press. (2012). *Introducing the new Kindle Paperwhite: The most advanced e-reader ever constructed.* Retrieved from [https://press.aboutamazon.com/2012/9/introducing-the-new-kindle-paperwhite-the-most-advanced-e-reader-ever-constructed/](https://press.aboutamazon.com/2012/9/introducing-the-new-kindle-paperwhite-the-most-advanced-e-reader-ever-constructed/)  

- The Verge. (2024). *Black Friday best deal: E-reader Kobo Libra Colour.* Retrieved from [https://www.theverge.com/2024/11/27/24307532/black-friday-best-deal-e-reader-kobo-libra-colour-cyber-monday](https://www.theverge.com/2024/11/27/24307532/black-friday-best-deal-e-reader-kobo-libra-colour-cyber-monday)  

- TIME. (2024). *An Artistic E-Reader.* Retrieved from [https://time.com/7094611/rakuten-kobo-libra-colour/](https://time.com/7094611/rakuten-kobo-libra-colour/)  

- USA Facts. (2024). *U.S. Population Data.* Retrieved from [https://usafacts.org/data/topics/people-society/population-and-demographics/our-changing-population/](https://usafacts.org/data/topics/people-society/population-and-demographics/our-changing-population/)  




