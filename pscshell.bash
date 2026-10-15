numver=0.0
strver="demo1"
package="./pscpackage"
definer="./pscpackage/define.py"
echo "PseudoScript v"$numver $strver""
cd $package
if pwd "$package"; then
    echo "The package was found! Welcome, user!"
else
    echo "Wheres the package? Perhaps an install.."
fi

echo "Welcome! Choose a command.."
select choice in Script Find GetPack Exit; do case choice in
    Script) curl https://stefanm03-sys.github.io/PseudoScript/ ;;
    Find) grep -i ".psc" ;;
    GetPack) echo "Getting that package.." ;;
    Exit) echo "Exiting shell.."; break;;
    *) echo "Invalidated! Try again.."
    esac
done
