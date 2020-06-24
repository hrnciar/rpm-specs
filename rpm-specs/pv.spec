Summary: A tool for monitoring the progress of data through a pipeline
Name: pv
Version: 1.6.6
Release: 8%{?dist}
License: Artistic 2.0
Source0: http://www.ivarch.com/programs/sources/%{name}-%{version}.tar.gz
URL: http://www.ivarch.com/programs/pv.shtml


BuildRequires:  gcc
BuildRequires: gettext


%description
PV ("Pipe Viewer") is a tool for monitoring the progress of data through a
pipeline.  It can be inserted into any normal pipeline between two processes
to give a visual indication of how quickly data is passing through, how long
it has taken, how near to completion it is, and an estimate of how long it
will be until completion.


%prep
%setup -q
mv README README.iso8859
iconv -f ISO-8859-1 -t UTF-8 README.iso8859  > README
mv doc/NEWS doc/NEWS.iso8859
iconv -f ISO-8859-1 -t UTF-8 doc/NEWS.iso8859 > doc/NEWS

%build
%configure
%make_build


%install
mkdir -p ${RPM_BUILD_ROOT}%{_bindir}         # /usr/bin
mkdir -p ${RPM_BUILD_ROOT}%{_mandir}/man1    # /usr/share/man/man1

%make_install
%find_lang %{name}


%check
make test


%files -f %{name}.lang
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.gz

%license doc/COPYING
%doc README doc/NEWS doc/TODO


%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Mar 15 2019 Orion Poplawski <orion@nwra.com> - 1.6.6-7
- Modernize spec
- Drop dependency on initscripts (usleep) (bugz#1592410)

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 10 2017 Jakub Hrozek <jhrozek@redhat.com> - 1.6.6-1
- New upstram release 1.6.6

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Mar 15 2015 Jakub Hrozek <jhrozek@redhat.com> - 1.6.0-1
- New upstream release

* Wed Aug 27 2014 Jakub Hrozek <jhrozek@redhat.com> - 1.5.7-1
- New upstream release

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue May 06 2014 Jakub Hrozek <jhrozek@redhat.com> - 1.5.3-1
- New upstream release

* Tue Feb 11 2014 Jakub Hrozek <jhrozek@redhat.com> - 1.5.2-1
- New upstream release

* Tue Aug 06 2013 Jakub Hrozek <jhrozek@redhat.com> - 1.5.1-1
- New upstream release

* Tue Aug 06 2013 Jakub Hrozek <jhrozek@redhat.com> - 1.4.12-1
- BuildRequire usleep so that unit tests can run safely

* Mon Aug 05 2013 Jakub Hrozek <jhrozek@redhat.com> - 1.4.6-3
- BuildRequire usleep so that unit tests can run safely

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Feb 25 2013 Jakub Hrozek <jhrozek@redhat.com> - 1.4.6-1
- New upstream release

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Oct 30 2012 Jakub Hrozek <jhrozek@redhat.com> - 1.3.8-1
- New upstream release

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jul 9 2012 Jakub Hrozek <jhrozek@redhat.com> - 1.3.4-1
- New upstream release

* Sat Jun 9 2012 Jakub Hrozek <jhrozek@redhat.com> - 1.3.1-1
- New upstream release

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Dec 14 2010 Jakub Hrozek <jhrozek@redhat.com> - 1.2.0-1
- New upstream release

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Mar 13 2008 Jakub Hrozek <jhrozek@redhat.com> - 1.1.4-1
- Bump to the latest upstream
- Convert NEWS and README to UTF8 during prep

* Mon Feb 11 2008 Jakub Hrozek <jhrozek@redhat.com> - 1.1.0-3
- Rebuild for GCC 4.3

* Sat Sep 15 2007 Jakub Hrozek <jhrozek@redhat.com> - 1.1.0-2
- Fix the license tag

* Sat Sep 15 2007 Jakub Hrozek <jhrozek@redhat.com> - 1.1.0-1
- Bump to the latest upstream

* Mon Aug 13 2007 Jakub Hrozek <jhrozek@redhat.com> - 1.0.1-1
- Bump to latest upstream

* Sun Jun 24 2007 Jakub Hrozek <jhrozek@redhat.com> - 0.9.9-1
- Initial packaging loosely based on SRPM from project's home page by 
  Andrew Wood <andrew.wood@ivarch.com>
