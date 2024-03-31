from vertexai.generative_models import GenerativeModel


class Gemini:
    def __init__(self):
        self.model = GenerativeModel("gemini-1.0-pro-vision")

    def multi_model_prompt(
        self,
        chlrophyll,
        DaytimeSST,
        NighttimeSST,
        PAR,
    ):
        response = self.model.generate_content(
            [
                chlrophyll,
                "Analyze the chlorophyll concentration data to determine the productivity of marine phytoplankton. High chlorophyll levels typically indicate rich biological activity and are foundational to the marine food chain. Assess how these levels vary spatially and temporally to understand the health and distribution of marine life in the region.",
                DaytimeSST,
                "Examine the daytime sea surface temperature data to evaluate the thermal conditions affecting marine life during daylight hours. Correlate these temperatures with the presence and behavior of various marine species, focusing on areas with optimal temperature ranges for coral reefs, fish, and plankton activity.",
                NighttimeSST,
                "Use the nighttime sea surface temperature data to gain insights into the stable thermal environment of the ocean. This measurement can provide a baseline for understanding the thermal preferences and stress thresholds of different marine organisms, particularly nocturnal and deep-water species.",
                PAR,
                "Review the photosynthetically available radiation data to gauge the energy available for photosynthesis in the ocean, which directly impacts the growth of phytoplankton and the overall primary productivity of the marine ecosystem. Relate PAR levels to the potential for supporting diverse and healthy marine life populations. If the marine enviroment is in danger, provide a solution to the problem. If the enviroment is healthy, provide a way to maintain it.",
            ]
        )
        return response.text
