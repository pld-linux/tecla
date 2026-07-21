Summary:	Tecla - keyboard layout viewer
Summary(pl.UTF-8):	Tecla - przeglądarka układów klawiatury
Name:		tecla
Version:	50.0
Release:	1
License:	GPL v2+
Group:		Libraries
Source0:	https://download.gnome.org/sources/tecla/50/%{name}-%{version}.tar.xz
# Source0-md5:	cc5ae49bae10abcb02040a20e63ef26b
URL:		https://gitlab.gnome.org/GNOME/tecla
BuildRequires:	gettext-tools
BuildRequires:	gtk4-devel >= 4.0
BuildRequires:	libadwaita-devel >= 1.4
BuildRequires:	meson >= 0.54
BuildRequires:	ninja >= 1.5
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpmbuild(macros) >= 2.042
BuildRequires:	tar >= 1:1.22
# wayland-client
BuildRequires:	wayland-devel
BuildRequires:	xorg-lib-libxkbcommon-devel
BuildRequires:	xz
Requires:	libadwaita >= 1.4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tecla is a keyboard layout viewer. It uses GTK/Libadwaita for UI, and
libxkbcommon to deal with keyboard maps.

%description -l pl.UTF-8
Tecla to przeglądarka układów klawiatury. Wykorzystuje biblioteki
GTK/Libadwaita do interfejsu użytkownika oraz libxkbcommon do obsługi
map klawiatury.

%package devel
Summary:	Development files for Tecla utility
Summary(pl.UTF-8):	Pliki programistyczne narzędzia Tecla
Group:		Development/Libraries
# doesn't require base - it's just for building apps checking tecla presence/path
Requires:	pkgconfig
BuildArch:	noarch

%description devel
Development files for Tecla utility.

%description devel -l pl.UTF-8
Pliki programistyczne narzędzia Tecla.

%prep
%setup -q

%build
%meson

%meson_build

%install
rm -rf $RPM_BUILD_ROOT

%meson_install

# not supported by glibc (as of 2.41)
%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/ie

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc NEWS README.md
%attr(755,root,root) %{_bindir}/tecla
%{_desktopdir}/org.gnome.Tecla.desktop
%{_iconsdir}/hicolor/scalable/apps/org.gnome.Tecla.svg
%{_iconsdir}/hicolor/symbolic/apps/org.gnome.Tecla-symbolic.svg

%files devel
%defattr(644,root,root,755)
%{_npkgconfigdir}/tecla.pc
