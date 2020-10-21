Summary:        Command line interface to the freedesktop.org trashcan
Name:           trash-cli
Version:        0.17.1.14
Release:        12%{?dist}
License:        GPLv2+
URL  :          https://github.com/andreafrancia/trash-cli
Source0:        https://files.pythonhosted.org/packages/source/t/%{name}/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  python3-setuptools
BuildRequires:  python3-devel
Requires:       python3-unipath
Requires:       python3-setuptools

%description
trash-cli provides a command line trash usable with GNOME, KDE, Xfce or any
freedesktop.org compatible trash implementation. The command line interface is
compatible with rm and you can use trash-put as an alias to rm.

%prep
%autosetup -n %{name}-%{version}

%build
%py3_build

%install
%py3_install

%files
%doc README.rst

%{_bindir}/trash*
%{python3_sitelib}/trashcli/
%{python3_sitelib}/trash_cli-*-py*.egg-info
%{_mandir}/man1/trash-*

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.17.1.14-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.17.1.14-11
- Rebuilt for Python 3.9

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.17.1.14-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.17.1.14-9
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.17.1.14-8
- Rebuilt for Python 3.8

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.17.1.14-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.17.1.14-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.17.1.14-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.17.1.14-4
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.17.1.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.17.1.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri May 5 2017 Jan Beran <jberan@redhat.com> 0.17.1.14-1
- Latest Python 3 upstream version

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.12.29-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Dec 30 2016 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.16.12.29-1
- Update to latest upstream release

* Fri Dec 30 2016 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.16.12.28-1
- Update to latest upstream version

* Tue Dec 27 2016 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.16.12.26-1
- Update to latest upstream version

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12.9.14-11git798b71d
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Mon Feb 15 2016 Ankur Sinha <ankursinha AT fedoraproject DOT org> 0.12.9.14-10git798b71d
- Update to latest git commit
- Add patches that are pending merge to fix #1291236

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.9.14-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12.9.14-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 30 2014 Toshio Kuratomi <toshio@fedoraproject.org> - 0.12.9.14-7
- Replace python-setuptools-devel BR with python-setuptools

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12.9.14-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12.9.14-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jun 18 2013 Rahul Sundaram <sundaram@fedoraproject.org> - 0.12.9.14-4
- drop use of pyver macro

* Tue Jun 18 2013 Rahul Sundaram <sundaram@fedoraproject.org> - 0.12.9.14-3
- fix URL. resolves rhbz#975373
- drop redundant clean, defattr and macro defs

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12.9.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Oct 26 2012 Ankur Sinha <ankursinha AT fedoraproject DOT org> 0.12.9.14-1
- Update to latest upstream release

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12.4.24-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Apr 25 2012 Ankur Sinha <ankursinha AT fedoraproject DOT org> 0.12.4.24-1
- Update to new release
- update source url

* Fri Jan 06 2012 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.11.3-0.5.r315
- spec bump for gcc 4.7 rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11.3-0.4.r315
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Feb 07 2011 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.11.3-0.3.r315
- Updated patch

* Sun Feb 06 2011 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.11.3-0.2.r315
- Add requires to python-setuptools
- Patch to correct trash-empty

* Tue Jan 04 2011 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.11.3-0.1.r315 
- update to latest up stream release
- http://pypi.python.org/pypi/trash-cli/
- rename restore-trash to trash-restore : refer comment

* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> - 0.11.2-3
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Thu Feb 18 2010 Rahul Sundaram <sundaram@fedoraproject.org> - 0.11.2-2
- Update as per review

* Fri Oct 23 2009 Rahul Sundaram <sundaram@fedoraproject.org> - 0.11.2-1
- new upstream release
- cleaned up spec

* Mon Jun 29 2009 Rahul Sundaram <sundaram@fedoraproject.org> - 0.11.1.2-1
- Updated spec for review

* Sat Mar 14 2009 Terje Rosten <terje.rosten@ntnu.no> - 0.11.0-1.r199
- initial build


