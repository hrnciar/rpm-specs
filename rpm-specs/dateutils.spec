Name:           dateutils
Version:        0.4.7
Release:        2%{?dist}
Summary:        Command-line date and time calculation, conversion, and comparison

License:        BSD
URL:            http://www.fresse.org/dateutils/
Source0:        https://github.com/hroptatyr/dateutils/releases/download/v%{version}/%{name}-%{version}.tar.xz

# Upstream fix for include issue. https://github.com/hroptatyr/dateutils/issues/109
Patch0:         https://github.com/hroptatyr/dateutils/commit/6813ed94534f2311fbe9164748919e39d60b0190.patch

Requires(post):  info
Requires(preun): info

BuildRequires:  gcc

%description
Tools which revolve around fiddling with dates and times on the command
line, with a strong focus on use cases that arise when dealing with large
amounts of financial data.


%prep
%autosetup -p1


%build
%configure --disable-silent-rules --without-old-links
# see note in configure script for why we're passing CFLAGS explicitly here
make %{?_smp_mflags} CFLAGS="$CFLAGS"


%install
%make_install

rm -f %{buildroot}%{_infodir}/dir
# this is duplicated otherwise
rm -f %{buildroot}%{_datadir}/doc/%{name}/LICENSE


%check
make check

%files
%license LICENSE
%doc README.md
%{_bindir}/*
%{_mandir}/man1/*
%{_infodir}/%{name}*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*.tzmcc
%{_datadir}/%{name}/locale


%changelog
* Wed Apr 29 2020 Matthew Miller <mattdm@fedoraproject.org> - 0.4.7-2
- pull in upstream patch for build issue
- use autosetup macro to apply patches. fun new stuff for old packagers!

* Wed Apr 29 2020 Matthew Miller <mattdm@fedoraproject.org> - 0.4.7-1
- upstream 0.4.7 bugfix release

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Mar 20 2019 Matthew Miller <mattdm@fedoraproject.org> - 0.4.6-1
- upstream 0.4.6 bugfix release

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Nov  5 2018 Matthew Miller <mattdm@fedoraproject.org> - 0.4.5-1
- upstream 0.4.5 bugfix release

* Tue Aug 14 2018 Matthew Miller <mattdm@fedoraproject.org> - 0.4.4-1
- upstream 0.4.4 bugfix release

* Sun Jul 22 2018 Matthew Miller <mattdm@fedoraproject.org> - 0.4.3-3
- add gcc to buildreqs

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Mar  1 2018 Matthew Miller <mattdm@fedoraproject.org> - 0.4.3-1
- 0.4.3 upstream feature release "base expansion works for times now"
- also minor bugfixes

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 24 2017 Matthew Miller <mattdm@fedoraproject.org> - 0.4.2-1
- upstream release which fixes dst translation bug
- new feature: allow format specifiers to turn off padding (as GNU date does)
- new feature: matlab-style day numbers

* Fri Aug 04 2017 Matthew Miller <mattdm@fedoraproject.org> - 0.4.1-8
- aha. upstream fix to handle tz dst transition format change

* Fri Aug 04 2017 Matthew Miller <mattdm@fedoraproject.org> - 0.4.1-7
- works with local mock build; fails in koji. i dunno :-/

* Fri Aug 04 2017 Matthew Miller <mattdm@fedoraproject.org> - 0.4.1-6
- more diagnostic changes to figure out why that one test is failing

* Fri Aug 04 2017 Matthew Miller <mattdm@fedoraproject.org> - 0.4.1-5
- diagnostic changes to figure out why that one test is failing

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Dec 13 2016 Matthew Miller <mattdm@fedoraproject.org> - 0.4.1-1
- upstream minor bugfix release 0.4.1

* Thu Jun  2 2016 Matthew Miller <mattdm@fedoraproject.org> - 0.4.0-1
- update to 0.4.0
- new "--isvalid" feature for datetest
- locale-based input and output
- various bugfixes

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 22 2016 Matthew Miller <mattdm@fedoraproject.org> - 0.3.5-1
- update to upstream 0.3.5 release (small bugfixes)

* Tue Sep  1 2015 Matthew Miller <mattdm@fedoraproject.org> - 0.3.4-1
- update to upstream 0.3.4 release (bugfixes)

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 12 2015 Matthew Miller <mattdm@fedoraproject.org> - 0.3.3-3
- fix missing changelog. now with more changelog!
- don't duplicate the LICENSE file

* Thu Jun 11 2015 Matthew Miller <mattdm@fedoraproject.org> - 0.3.3-2
- fix dist -> ?dist

* Thu Jun 11 2015 Matthew Miller <mattdm@fedoraproject.org> - 0.3.3-1
- update to upstream 0.3.3 release; no more need for snapshots

* Mon Apr 27 2015 Matthew Miller <mattdm@fedoraproject.org> - 0.3.2.git37.96a5495-1
- newer upstream snapshot
- upstream fixed the short-name manpages problem
- add comment on where snapshot comes from in git

* Wed Apr 22 2015 Matthew Miller <mattdm@fedoraproject.org> - 0.3.2.git35.3e322eb-4
- treat upstream snapshot as minor release rather than snapshot
- temporary workaround to remove old short-name manpages

* Tue Apr 21 2015 Matthew Miller <mattdm@fedoraproject.org> - 0.3.2-3.git35.3e322eb
- use upstream snapshot tarball instead of patch

* Thu Apr 16 2015 Matthew Miller <mattdm@fedoraproject.org> - 0.3.2-2.20150415git%
- pull in patches from upstream to address potential name
  conflict with EL package + other minor issues
- include LICENSE as upstream now does (with this patch)

* Thu Mar 05 2015 Matthew Miller <mattdm@fedoraproject.org> - 0.3.2-1
- update to latest version

* Thu Mar  5 2015 Matthew Miller <mattdm@fedoraproject.org> 0.3.1-2
- add make check
- cflags fix

* Tue Mar  3 2015 Matthew Miller <mattdm@fedoraproject.org> 0.3.1-1
- initial package
