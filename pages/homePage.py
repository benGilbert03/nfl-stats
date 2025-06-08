import tkinter as tk
from tkinter import ttk
from fetchPlayers import getWeekOneStarters



class HomePage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        welcomeLabel = tk.Label(self, text='Rank Your Top NFL Players', font=('Arial', 18), )
        welcomeLabel.pack(pady=10)
        
        instrFrame = tk.Frame(self)
        instrFrame.pack()
        
        comboFrame = tk.Frame(self)
        comboFrame.pack()

        posChoiceInstr = tk.Label(instrFrame, text='Choose a position')
        yearChoiceInstr= tk.Label(instrFrame, text='Choose a year')

        posChoiceInstr.pack(side='left', padx=20)
        yearChoiceInstr.pack(side='right', padx=20)

        posCombobox = ttk.Combobox(comboFrame, values=['QB', 'RB', 'WR', 'TE', 'DB'])
        posCombobox.pack(side='left', padx=10)

        yearCombobox = ttk.Combobox(comboFrame, values=[2024, 2023, 2022, 2021, 2020, 2019, 2018, 2017, 2016, 2015, 2014, 2013, 2012, 2011])
        yearCombobox.pack(side='right', padx=10)


        submitButton = tk.Button(self, text='Submit Choices', command=lambda: self.submitChoices(posCombobox.get(), yearCombobox.get(), controller))
        submitButton.pack(pady=10)


    def submitChoices(self, pos, year, controller):
        try:
            year = int(year)
        except ValueError as e:
            print('Could not cast year to an int')
            return
        controller.sharedData['players'] = getWeekOneStarters([year], [pos])

        compPage = controller.frames['ComparisonsPage']
        controller.show_frame("ComparisonsPage")
        compPage.loopThroughPlayers(controller)

        