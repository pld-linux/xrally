Summary:	clone of the Rally X arcade game
Name:		xrally
Version:	0.9
Release:	1
License:	GPL
Group:		X11/Games
Group(pl):	X11/Gry
Source0:	ftp://ftp.linuxgames.com/xrally/%{name}-%{version}.tar.gz
Patch0:		xrally-DESTDIR.patch
URL:		http://www.linuxgames.com/xrally/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
XRally is a clone of the Rally X arcade game. In Rally X, you control a
blue car which has to run through a maze-like level collecting flags and
avoiding colliding with enemy (red) cars. In order to protect itself, the
blue car can discharge clouds of smoke which stun the enemy cars for a
while. The enemy cars can also crash into each other, what gives you some
extra time. One of the main features of XRally is that it is fully
customizable. You can create custom tilesets and levels and load them at
run time, changing the entire look of the game. (You could, for instance,
create a water tileset, using boats instead of cars.)

%prep
%setup -q -n %{name}
%patch -p1
rm maps/"Test Level"

%build
automake
LDFLAGS="-s"; export LDFLAGS
%configure
make CFLAGS="%{optflags}"

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install

gzip -9nf AUTHORS BUGS NEWS README TODO %{name}.lsm

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%{_datadir}/xrally
