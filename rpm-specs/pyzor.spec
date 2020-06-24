%global forgeurl https://github.com/SpamExperts/pyzor
%global commit f46159bd6519cebcebf59e9334a7920371111d75

Name:       pyzor
Version:    1.0.0
Release:    23%{?dist}
Summary:    Collaborative spam filtering system
License:    GPLv2
%forgemeta
URL:        %forgeurl
Source0:    %forgesource

BuildArch:     noarch
BuildRequires: python3-devel python3-pytest-cov
# No python3-redis (yet?) in EPEL, only in Fedora
%if 0%{?fedora}  
BuildRequires: python3-redis
%endif

%description
Pyzor is a collaborative, networked system to detect
and block spam using identifying digests of messages.
Pyzor is similar to Vipul's Razor except implemented
in python, and using fully open source servers.

Pyzor can be used either standalone, or to augment the
spam filtering ability of spamassassin.  spamassassin
is highly recommended.


%prep
%forgeautosetup -p1


%build
%py3_build


%install
%py3_install
install -d -m 755 %buildroot/etc/pyzor


# Tests are failing without python3-redis, even it's optional
%if 0%{?fedora}
%check
py.test-3 tests/unit/ --cov pyzor --cov-report term-missing
%endif


%files
%python3_sitelib/pyzor*
%license COPYING
%doc config/ README.rst THANKS
/etc/pyzor/
/usr/bin/pyzor*


%changelog
* Fri May 29 2020 Jason L Tibbitts III <tibbs@math.uh.edu> - 1.0.0-23.20200530gitf46159b
- Update to current git snapshot (fixes python 3.9 build).
- Remove merged patch.

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.0.0-22
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.0-20
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.0-19
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-17.git2b8d76d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jul 24 2018 Jason L Tibbitts III <tibbs@math.uh.edu> - 1.0.0-16.20180724git2b8d76d
- Update to current git snapshot, which has some python3 fixes.
- Include an additional python3 fix.
- Use modern py3 macros.
- Use forge macros.
- Minor spec cleanups.

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-15.20160210gitf16e1b6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.0.0-14.20160210gitf16e1b6
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-13.20160210gitf16e1b6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-12.20160210gitf16e1b6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-11.20160210gitf16e1b6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.0.0-10.20160210gitf16e1b6
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-9.20160210gitf16e1b6
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Wed Feb 10 2016 Jason L Tibbitts III <tibbs@math.uh.edu> - 1.0.0-8.20160210git
- Call as much of the test suite as we can.

* Wed Feb 10 2016 Jason L Tibbitts III <tibbs@math.uh.edu> - 1.0.0-7.20160210git
- Update to current git snapshot.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Dec 07 2015 Jason L Tibbitts III <tibbs@math.uh.edu> - 1.0.0-5
- Use github site as upstream instead of sourceforge.

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Mar 06 2015 Jason L Tibbitts III <tibbs@math.uh.edu> - 1.0.0-2
- Upstream clarified that the license is indeed GPLv2:
  https://github.com/SpamExperts/pyzor/issues/35

* Thu Mar 05 2015 Jason L Tibbitts III <tibbs@math.uh.edu> - 1.0.0-1
- Update to 1.0.0.
- Clean up and greatly simplify the specfile.
- Use python3 as the program supports it.

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> - 0.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Thu Nov 05 2009 Warren Togami <wtogami@redhat.com> - 0.5.0-3
- -Wignore::DeprecationWarning to make it work (#531653)

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu May 14 2009 Andreas Thienemann <andreas@bawue.net> - 0.5.0-1
- Update to new upstream release 0.5.0
- Dropped unnecessary patches

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 0.4.0-14
- Rebuild for Python 2.6

* Thu Aug 14 2008 Jason L Tibbitts III <tibbs@math.uh.edu> - 0.4.0-13
- Fix failing build too.

* Thu Aug 14 2008 Jason L Tibbitts III <tibbs@math.uh.edu> - 0.4.0-12
- Fix license tag.

* Sat Dec 23 2006 Jason L Tibbitts III <tibbs@math.uh.edu> - 0.4.0-11
- Rebuild with Python 2.5.

* Fri Sep 08 2006 Andreas Thienemann <andreas@bawue.net> - 0.4.0-10
- FE6 Rebuild
- Feature enhancements by including certain patches from swinog.

* Mon Feb 07 2005 Toshio Kuratomi <toshio@tiki-lounge.com> - 0.4.0-8
- %%ghost *.pyo files.

* Sat Feb 05 2005 Toshio Kuratomi <toshio@tiki-lounge.com> - 0.4.0-7
- Use python_sitelib macro to fix building on x86_64.
- Change byte compile argumetns so we don't encode the buildroot into the
  byte compiled python files.
- Use python-abi for Requires instead of python package.

* Sat Nov 13 2004 Warren Togami <wtogami@redhat.com> - 0.4.0-6
- bump release

* Fri May 21 2004 Warren Togami <wtogami@redhat.com> - 0.4.0-0.fdr.5
- generalize python version

* Fri Jul 11 2003 Warren Togami <warren@togami.com> - 0.4.0-0.fdr.4
- Change to __python macro

* Fri Jun 27 2003 Warren Togami <warren@togami.com> - 0.4.0-0.fdr.3
- #360 add more docs

* Sat Jun 21 2003 Warren Togami <warren@togami.com> - 0.4.0-0.fdr.2
- Fix some directory macros
- #360 Include .pyc and .pyo so package removes cleanly
- #360 install -p preserve timestamps

* Sun Jun 08 2003 Warren Togami <warren@togami.com> - 0:0.4.0-0.fdr.1
- Convert to Fedora

* Fri Jan 31 2003 Shad L. Lords <slords@mail.com>
- 0.4.0-1
- inital release
