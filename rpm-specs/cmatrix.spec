# fonts folder managed in xorg-x11-fonts but we don't want to enforce everything
%global _x11fontdir %{_datadir}/X11/fonts

%global aurgiturl    https://git.archlinux.org/svntogit/community.git

Name:                cmatrix
Version:             1.2a
Release:             7%{?dist}
Summary:             A scrolling 'Matrix'-like screen

License:             GPLv2+
URL:                 http://www.asty.org/%{name}
Source0:             %{url}/dist/%{name}-%{version}.tar.gz
Source1:             %{aurgiturl}/plain/trunk/%{name}-tty?h=packages/%{name}#/%{name}-tty

BuildRequires:       gcc
BuildRequires:       pkgconfig(ncurses)
BuildRequires:       help2man


%description
Let's see the cool scrolling lines from the famous movie 'The Matrix'.


%package x11-fonts
Summary:            The font of 'Matrix' for X11

Requires(post):     mkfontdir
Requires(postun):   mkfontdir

%if 0%{?fedora}
Suggests:           xorg-x11-fonts
%endif

%description x11-fonts
The font seen in the famous movie 'The Matrix' to be used in X11.


%prep
%autosetup
cp -p %{SOURCE1} .
# install fonts properly
sed -i -r 's: (%{_prefix}): \$(DESTDIR)\1:' Makefile.in


%build
%configure
%make_build
help2man -N -o %{name}.1 ./%{name}


%install
install -dm0755 %{buildroot}%{_datadir}/consolefonts
%make_install
install -Dpm0644 mtx.pcf %{buildroot}%{_x11fontdir}/misc/mtx.pcf
install -Dm755 %{name}-tty %{buildroot}%{_bindir}
install -Dpm0644 %{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1


%post x11-fonts
mkfontdir %{_x11fontdir}/misc

%postun x11-fonts
if [ "$1" = "0" -a -d %{_x11fontdir}/misc ]; then
  mkfontdir %{_x11fontdir}/misc
fi


%files
%license COPYING
%doc AUTHORS NEWS README ChangeLog TODO
%{_bindir}/%{name}
%{_bindir}/%{name}-tty
# we don't want to depend on other consolefonts
%dir %{_datadir}/consolefonts
%{_datadir}/consolefonts/matrix.*
%{_mandir}/man1/%{name}.1*

%files x11-fonts
# we don't want to depend on other x11 fonts
%dir %{_x11fontdir}
%dir %{_x11fontdir}/misc
%{_x11fontdir}/misc/mtx.pcf
%{_mandir}/man1/%{name}.1*


%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2a-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2a-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2a-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2a-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2a-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2a-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jun 17 2017 Raphael Groner <projects.rg@smart.ms> - 1.2a-1
- initial
