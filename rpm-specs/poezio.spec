Name:		poezio
Version:	0.12.1
Release:	5%{?dist}
Summary:	IRC-like jabber (XMPP) console client

License:	zlib
URL:		http://poez.io
Source0:    https://lab.louiz.org/%{name}/%{name}/-/archive/v%{version}/%{name}-v%{version}.tar.bz2


BuildRequires:	python3-devel
BuildRequires:	gcc
Requires:       python3-slixmpp
Requires:       python3-inotify


%description
A jabber (XMPP) console client that aims at being similar to popular IRC
clients such as Irssi or Weechat. Its main goal is to let the user
connect to the Jabber network and join chat rooms without requiring any
registration.


%package -n %{name}-doc
Summary:    Documentation for Poezio
BuildArch:  noarch
Requires:   poezio

%description -n %{name}-doc
A jabber (XMPP) console client that aims at being similar to popular IRC
clients such as Irssi or Weechat. Its main goal is to let the user
connect to the Jabber network and join chat rooms without requiring any
registration.

This package contains documentation in reST format.



%prep
%autosetup -n %{name}-v%{version}


%build
%py3_build


%install
%py3_install

mv -f %{buildroot}%{_pkgdocdir}/source/ %{buildroot}%{_pkgdocdir}/rst/


%files
%license COPYING
%doc CHANGELOG README.rst
%{_bindir}/%{name}
%{_bindir}/%{name}_logs
%{_datadir}/%{name}/
%{_mandir}/man1/%{name}.1*
%{_mandir}/man1/%{name}_logs.1*
%{python3_sitearch}/%{name}/
%{python3_sitearch}/%{name}_plugins/
%{python3_sitearch}/%{name}_themes/
%{python3_sitearch}/%{name}-*.egg-info


%files -n %{name}-doc
%{_pkgdocdir}/rst/



%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.12.1-4
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.12.1-2
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Sun Aug 25 2019 Matthieu Saulnier <fantom@fedoraproject.org> - 0.12.1-1
- Update to 0.12.1
  - undo commit c4143e60552024c87941da00c249792422de9085 (sitelib vs sitearch)
  - undo commit 4ae44ca7eda1d027c4c3559679edf6d970a9ed7c (Disable debuginfo)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.12-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Aug 17 2018 Florent Le Coz <louiz@louiz.org> - 0.12-1
- Update to 0.12
- Remove the HTML doc because it’s absent from the archive now

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.11-2
- Rebuilt for Python 3.7

* Sat Apr 28 2018 Matthieu Saulnier <fantom@fedoraproject.org> - 0.11-1
- Update to 0.11 stable release
- Split html doc and rst doc files in doc subpackage

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-0.11.dfd6042
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-0.10.dfd6042
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-0.9.dfd6042
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-0.8.dfd6042
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.9-0.7.dfd6042
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-0.6.dfd6042
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-0.5.dfd6042
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Nov 19 2015 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.9-0.4.dfd6042
- Remove sources from documentation directory
- Use %%license macro

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-0.3.dfd6042
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-0.2.dfd6042
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri May 08 2015 Matthieu Saulnier <fantom@fedoraproject.org> - 0.9-0.1.dfd6042
- Update to 0.9 prerelease with upstream git snapshot

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Wed Jul 30 2014 Matthieu Saulnier <fantom@fedoraproject.org> - 0.8.1-1
- Update to 0.8.1 stable release

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May 22 2014 Bohuslav Kabrda <bkabrda@redhat.com> - 0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Sat Feb 22 2014 Matthieu Saulnier <fantom@fedoraproject.org> - 0.8-1
- Update to 0.8 stable release

* Tue Nov 26 2013 Matthieu Saulnier <fantom@fedoraproject.org> - 0.8-0.6.20131126git1ac0367
- Update to latest revision
- Update license tag
- Update url tag
- Add new theme directory in %%file section
- Remove %%{_docdir} line to fix duplicate files in package

* Sun Oct 27 2013 Matthieu Saulnier <fantom@fedoraproject.org> - 0.8-0.5.20131021git4a091b3
- Update to latest revision

* Tue Aug 06 2013 Matthieu Saulnier <fantom@fedoraproject.org> - 0.8-0.4.20130806git703cd1b
- Update to latest revision

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-0.3.20130701gitf8aa0f9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jul 01 2013 Matthieu Saulnier <fantom@fedoraproject.org> - 0.8-0.2.20130701gitf8aa0f9
- Update to latest revision

* Thu Jun 06 2013 Matthieu Saulnier <fantom@fedoraproject.org> - 0.8-0.1.20130606git9e8860c
- Update to 0.8 with upstream git snapshot
- Add python3 macro to bytecompile with the correct python version
- Remove obsolete Group tag
- Remove obsolete BuildRoot tag
- Remove BuildArch tag
- Update Requires and BuildRequires tags
- Update %%setup command for new Source
- Remove obsolete %%clean section
- Remove obsolete %%defattr line in %%files section

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Aug 11 2010 Le Coz Florent <louizatakk@fedoraproject.org> - 0.6.2-3
- Some minor changes to the .spec file from the Review Request on rhbz

* Sat Jul 24 2010 Le Coz Florent <louizatakk@fedoraproject.org> - 0.6.2-2
- Add python2-devel to BuildRequires

* Fri Jul 23 2010 Le Coz Florent <louizatakk@fedoraproject.org> - 0.6.2-1
- Update sources to 0.6.2

* Sat Jun 19 2010 Le Coz Florent <louizatakk@fedoraproject.org> - 0.6.1-1
- Spec file written from scratch
