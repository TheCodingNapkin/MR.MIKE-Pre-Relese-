import cx_Freeze

executables = [cx_Freeze.Executable("MRMIKE.py")]

cx_Freeze.setup(
    name="Mr.Mike Get Over Here! (MMP)",
    options={"build_exe": {"packages":["pygame"],
                           "include_files":["car1.png","car2.png","car3.png","dance1.png","dance2.png","dance3.png","dance4.png","dance5.png","dance6.png","dance7.png","dance8.png","dance9.png","dance10.png","dance11.png","dance12.png","dance13.png","dance14.png","dance15.png","dance16.png","dance17.png","dance18.png","dance19.png","dance20.png","dance21.png","dance22.png","dance23.png","dance24.png","dance25.png","dance26.png","dance27.png","face1.png","face2.png","face3.png","face4.png","icon1.png","Lamboveiw1.png","Lamboveiw2.png","MobBoss.png","player1.png","player2.png","player3.png","player4.png","Player1.txt","Player2.txt","Raleway-Medium.ttf"]}},
    executables = executables
    )

