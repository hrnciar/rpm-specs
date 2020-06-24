Name:           sawfish-pager
Version:        0.90.4
Release:        13%{?dist}
Summary:        Pager for Sawfish window manager
License:        GPLv2+
URL:            http://sawfish.wikia.com/
Source0:        http://download.tuxfamily.org/sawfishpager/%{name}_%{version}.tar.bz2
BuildRequires:  gcc
BuildRequires:  gmp-devel
BuildRequires:  gtk2-devel
BuildRequires:  sawfish-devel >= 1.8.1
Requires:       sawfish >= 1.8.1


%description
Sawfish specific configurable pager map of your desktop with a
viewport support. It can be configured to follow where you are, or
optionally show all workspaces at once.

Check README from this package documentation how to activate.


%prep
%setup -q -n %{name}_%{version}


%build
%configure
make %{?_smp_mflags}


%install
%make_install


%files
%license COPYING
%doc NEWS README TODO
%{_libdir}/sawfish/sawfishpager
%{_datadir}/sawfish/lisp/sawfish/wm/ext/*


%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.90.4-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.90.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.90.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 14 2019 Björn Esser <besser82@fedoraproject.org> - 0.90.4-10
- Rebuilt for libcrypt.so.2 (#1666033)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.90.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.90.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 20 2018 Björn Esser <besser82@fedoraproject.org> - 0.90.4-7
- Rebuilt for switch to libxcrypt

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.90.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.90.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.90.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.90.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.90.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Nov  4 2014 Kim B. Heino <b@bbbs.net> - 0.90.4-1
- Update to 0.90.4

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.90.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.90.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.90.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.90.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.90.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Mar 26 2012 Kim B. Heino <b@bbbs.net> - 0.90.3-1
- Update to 0.90.3

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.90.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Nov  2 2011 Kim B. Heino <b@bbbs.net> - 0.90.2-4
- Rebuild

* Mon Aug 15 2011 Kim B. Heino <b@bbbs.net> - 0.90.2-3
- Don't update COPYING

* Sun Aug 14 2011 Kim B. Heino <b@bbbs.net> - 0.90.2-2
- Update COPYING file for correct FSF address
- Simplify BuildRequires

* Wed Jun 22 2011 Kim B. Heino <b@bbbs.net> - 0.90.2-1
- Update to 0.90.2

* Fri Apr 15 2011 Kim B. Heino <b@bbbs.net> - 0.90.1-2
- Update buildrequirements

* Sat Apr  2 2011 Kim B. Heino <b@bbbs.net> - 0.90.1-1
- Update to 0.90.1

* Sat Jan 23 2010 Kim B. Heino <b@bbbs.net> - 0.7.3-1
- fix rpmlint warnings

* Fri Jan 22 2010 Michal Jaegermann <michal@harddata.com> - 0.7.2-1
- Initial build.
