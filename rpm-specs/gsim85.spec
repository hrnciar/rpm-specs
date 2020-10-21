Name:           gsim85
Version:        0.3
Release:        25%{?dist}
Summary:        An 8085 microprocessor simulator

License:        GPLv2+
URL:            http://gsim85.sourceforge.net/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Patch0:         gsim85-0.3-format-security.patch

BuildRequires:  gcc
BuildRequires:  libglade2-devel
BuildRequires:  intltool
BuildRequires:  perl-XML-Parser
BuildRequires:  desktop-file-utils

Requires:       electronics-menu

%description
It is an 8085 simulator. It is having very user friendly graphical
user interface. It can be used to test 8085 programs before actualy
implementing them on target board.

%prep
%setup -q
%patch0 -p1 -b .error

%build
%configure --disable-static
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot} INSTALL="install -p"
desktop-file-install                                    \
    --remove-category="IDE;Development;Engineering;"    \
    --add-category="Electronics;"                       \
    --dir=%{buildroot}%{_datadir}/applications          \
    %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%{_pkgdocdir}
%exclude %{_pkgdocdir}/COPYING
%exclude %{_pkgdocdir}/INSTALL
%license COPYING
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/pixmaps/gsim.png
%{_datadir}/pixmaps/%{name}/
%{_datadir}/applications/%{name}.desktop

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 12 2016 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.3-16
- Let package install docs (Fix F24FTBFS).
- Don't ship INSTALL.
- Add %%license.

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon Jun 23 2014 Yaakov Selkowitz <yselkowi@redhat.com> - 0.3-12
- Fix FTBFS with -Werror=format-security (rhbz#1037107, rhbz#1106733)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Aug 05 2013 Fabian Affolter <mail@fabian-affolter.ch> - 0.3-10
- Spec file updated
- Fixed FTBFS (#992437)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Jan 07 2013 Fabian Affolter <mail@fabian-affolter.ch> - 0.3-7
- Minor changes to match updated guidelines

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 0.3-4
- Rebuild for new libpng

* Fri Aug 12 2011 Fabian Affolter <mail@fabian-affolter.ch> - 0.3-3
- Rebuild (libglade)

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Aug 07 2009 Fabian Affolter <mail@fabian-affolter.ch> - 0.3-1
- Removed wrong end of line encoding fix
- Removed permission fix
- Removed patch0, replaced with desktop-file-install
- Updated to new upstream version 0.3

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun Jun 28 2009 Fabian Affolter <mail@fabian-affolter.ch> - 0.2-5
- Fixed the place in the menu

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Feb 08 2009 Fabian Affolter <mail@fabian-affolter.ch> - 0.2-3
- Fixed license tag, it's GPLv2+

* Wed Feb 04 2009 Fabian Affolter <mail@fabian-affolter.ch> - 0.2-2
- Added patch for desktop file
- Removed duplicate BR
- Preserved time stamps

* Tue Feb 03 2009 Fabian Affolter <mail@fabian-affolter.ch> - 0.2-1
- Initial package for Fedora
