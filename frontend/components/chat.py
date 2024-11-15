import reflex as rx
from frontend.components.product_cards import product_grid_for_in_chat_response
from states.chat_state import ChatState
from states.models.messages import Message, Role, FinishReason


def message_box(message: Message) -> rx.Component:
    return rx.cond(
        message.role == Role.USER,
        # Question
        rx.box(
            rx.markdown(
                message.content,
                class_name="[&>p]:!my-2.5",
            ),
            class_name="relative bg-slate-3 px-5 rounded-3xl max-w-[70%] text-slate-12 self-end",
        ),

        # Answer
        rx.box(
            rx.image(
                src="/chatgpt.png",
                class_name="h-6" + rx.cond(ChatState.processing, " animate-pulse", ""),
            ),
            rx.cond(
                message.type == FinishReason.STOP_TOKEN,
                rx.box(
                    rx.markdown(
                        message.content,
                        class_name="[&>p]:!my-2.5",
                    ),
                    class_name="relative bg-accent-3 px-5 rounded-3xl max-w-[70%] text-slate-12 self-start"
                ),
                rx.vstack(
                    rx.box(
                        rx.markdown(
                            message.content,
                            class_name="[&>p]:!my-2.5",
                        ),
                        class_name="relative bg-accent-3 px-5 rounded-3xl max-w-[70%] text-slate-12 self-start"
                    ),
                    rx.box(
                        product_grid_for_in_chat_response(),
                        class_name="relative bg-slate-4 px-5 rounded-3xl max-w-[70%] text-slate-12 self-start",
                        padding="10px"
                    )
                ),
            ),
            class_name="flex flex-row gap-6",
        ),
    )


def chat() -> rx.Component:
    return rx.scroll_area(
        rx.box(
            rx.foreach(
                ChatState.chat_history,
                message_box,
            ),
            class_name="flex flex-col gap-8 pb-10 group"
        ),
        scrollbars="vertical",
        class_name="w-full",
    )


def action_bar() -> rx.Component:
    return rx.box(
        rx.box(
            rx.el.input(
                placeholder="Ask anything",
                on_blur=ChatState.set_question,
                id="input1",
                class_name="box-border bg-slate-3 px-4 py-2 pr-14 rounded-full w-full outline-none focus:outline-accent-10 h-[48px] text-slate-12 placeholder:text-slate-9",
                on_key_down=ChatState.handle_key_down,
            ),
            rx.el.button(
                rx.cond(
                    ChatState.processing,
                    rx.icon(
                        tag="loader-circle",
                        size=19,
                        color="white",
                        class_name="animate-spin",
                    ),
                    rx.icon(tag="arrow-up", size=19, color="white"),
                ),
                on_click=[ChatState.answer, rx.set_value("input1", "")],
                class_name="top-1/2 right-4 absolute bg-accent-9 hover:bg-accent-10 disabled:hover:bg-accent-9 opacity-65 disabled:opacity-50 p-1.5 rounded-full transition-colors -translate-y-1/2 cursor-pointer disabled:cursor-default",
                disabled=rx.cond(
                    ChatState.processing | (ChatState.question == ""), True, False
                ),
            ),
            class_name="relative w-full",
        ),
        class_name="flex flex-col justify-center items-center gap-6 w-full",
    )
