Name:           trac-git-plugin
Version:        0.12.0.5
Release:        18.20111119git%{?dist}
Summary:        GIT version control plugin for Trac

License:        GPLv2+
URL:            http://trac-hacks.org/wiki/GitPlugin
# Source comes from github right now: git clone https://github.com/hvr/trac-git-plugin.git; \
#                                  cd trac-git-plugin/; \
#                                  echo "include COPYING" > MANIFEST.in; \
#                                  python setup.py sdist --formats gztar
Source0:        TracGit-%{version}dev-r0.tar.gz


BuildArch:      noarch
BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
Requires:       git-core, trac >= 0.12, python2-setuptools

%description
This Trac plugin provides support for the GIT SCM.

%prep
%setup -n TracGit-%{version}dev-r0 -q


%build
%py2_build


%install
rm -rf $RPM_BUILD_ROOT
# skip-build doesn't work on el4
%py2_install


 

%files
%doc COPYING README
# For noarch packages: sitelib
%{python2_sitelib}/*


%changelog
* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.0.5-18.20111119git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.0.5-17.20111119git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.0.5-16.20111119git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.0.5-15.20111119git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.0.5-14.20111119git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Feb 04 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.12.0.5-13.20111119git
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.0.5-12.20111119git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.0.5-11.20111119git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.0.5-10.20111119git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Dec 26 2015 Kevin Fenzi <kevin@scrye.com> - 0.12.0.5-9.20111119git
- Update to latest snapshot

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12.0.5-8.20101208git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12.0.5-7.20101208git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12.0.5-6.20101208git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12.0.5-5.20101208git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12.0.5-4.20101208git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12.0.5-3.20101208git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12.0.5-2.20101208git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 08 2010 Jesse Keating <jkeating@redhat.com> - 0.12.0.5-1.20101208git
- Update for trac-0.12
- New upstream source repo

* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> - 0.11.0.2-6.20090511svn5396
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11.0.2-5.20090511svn5396
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon May 11 2009 Jesse Keating <jkeating@redhat.com> - 0.11.0.2-2.20090511svn5396
- Drop COPYING, it doesn't make it into the tarball.

* Mon May 11 2009 Jesse Keating <jkeating@redhat.com> - 0.11.0.2-1.20090511svn5396
- Update for trac 0.11.  Drop patches as those are in the 0.11 branch.

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.1-8.20070705svn1536
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 0.0.1-7.20070705svn1536
- Rebuild for Python 2.6

* Mon Sep  8 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.0.1-6.20070705svn1536
- fix license tag

* Fri May 16 2008 Jesse Keating <jkeating@redhat.com> - 0.0.1-5.20070705svn1536
- Add patches from http://nanosleep.org/proj/trac-git-plugin

* Mon Nov 26 2007 Jesse Keating <jkeating@redhat.com> - 0.0.1-4.20070705svn1536
- Add a patch to prevent tracebacks when using this plugin

* Thu Jul 05 2007 Jesse Keating <jkeating@redhat.com> - 0.0.1-3.20070705svn1536
- Require trac and python-setuptools as well

* Thu Jul 05 2007 Jesse Keating <jkeating@redhat.com> - 0.0.1-2.20070705svn1536
- Require git-core

* Thu Jul 05 2007 Jesse Keating <jkeating@redhat.com> - 0.0.1-1.20070705svn1536
- Initial build
