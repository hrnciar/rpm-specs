%global pkg evil
%global pkgname Evil

Name:		emacs-%{pkg}
Version:	1.2.14
Release:	4%{?dist}
Summary:	Extensible vi layer for Emacs	
Summary(fr):	Surcouche vi extensible pour Emacs

License:	GPLv3+	
URL:		https://bitbucket.org/lyro/evil/wiki/Home
# Sources are checked out with git
Source0:	%{pkg}-%{version}.tar.xz
# Script to get the sources
Source1:    get_source.sh

BuildArch:	noarch
BuildRequires:	emacs
Requires:	emacs(bin) >= %{_emacs_version}
Requires:	emacs-goto-chg, emacs-undo-tree

%description
%{pkgname} is an extensible vi layer for GNU Emacs. It provides Vim features
like Visual selection and text objects, and is the successor of Vimpulse and
vim-mode.


%description -l fr
%{pkgname} est une surcouche vi extensible pour GNU Emacs. Il fournit des
fonctionnalités de Vim comme la sélection visuelle et les objets texte, et est
le successeur de Vimpulse et de vim-mode.


%prep
%setup -q -n %{pkg}

%build
make %{?_smp_mflags}

%check
# The tests launch emacs, so we need script to make it think we are in a tty.
script -ec "make tests" /dev/null

%install
mkdir -p $RPM_BUILD_ROOT%{_emacs_sitelispdir}/%{pkg}
cp -p *.el *.elc $RPM_BUILD_ROOT%{_emacs_sitelispdir}/%{pkg}

%files
%doc doc/evil.pdf COPYING
%{_emacs_sitelispdir}/%{pkg}

%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.14-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jun 13 2019 Willmann Sébastien <sebastien.willmann@gmail.com> - 1.2.14-1
- Update to version 1.2.14

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 07 2018 Willmann Sébastien <sebastien.willmann@gmail.com> - 1.2.13-1
- Updated to version 1.2.13

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Feb 06 2016 Sébastien Willmann <sebastien.willmann@gmail.com> - 1.2.9-1
- Update to version 1.2.9
- Changed project URL

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jan 07 2016 Sébastien Willmann <sebastien.willmann@gmail.com> - 1.2.8-1
- Update to version 1.2.8

* Mon Aug 17 2015 Sébastien Willmann <sebastien.willmann@gmail.com> - 1.2.3-1
- Update to version 1.2.3

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Apr 13 2014 sebastien.willmann@gmail.com - 1.0.9-1
- Update to version 1.0.9

* Sun Dec 22 2013 sebastien.willmann@gmail.com - 1.0.8-1
- Update to version 1.0.8

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Mar 17 2013 Sébastien Willmann <sebastien.willmann@gmail.com> - 1.0.1-1
- Update to version 1.0.1

* Wed Feb 20 2013 Sebastien Willmann <sebastien.willmann@gmail.com> - 1.0.0-1
- Update to release 1.0.0

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-0.6.20121003gitdcb8ebc
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Nov 05 2012 Sébastien Willmann <sebastien.willmann@gmail.com> - 0.1-0.5.20121003gitdcb8ebc
- Update to revision dcb8ebc
- Added tests

* Sat Nov 03 2012 Sébastien Willmann <sebastien.willmann@gmail.com> - 0.1-0.4.20121003gitf1b0789
- Update to revision f1b0789

* Sun Sep 02 2012 Sébastien Willmann <sebastien.willmann@gmail.com> - 0.1-0.3.20120902gitc13b90e
- Update to revision c13b90e

* Sat Aug 04 2012 Sébastien Willmann <sebastien.willmann@gmail.com> - 0.1-0.2.20120804gitd0cb72b
- Checked out new version with license notice in all source files.
- Changed license to GPLv3+
- Added goto-chg and undo-tree in Requires

* Sun Jul 29 2012 Sébastien Willmann <sebastien.willmann@gmail.com> - 0.1-0.1.20120729git052e701
- Initial spec file

