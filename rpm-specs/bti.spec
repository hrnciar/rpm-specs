Name:           bti
Version:        034
Release:        19%{?dist}
Summary:        Bash Twitter Idiocy

License:        GPLv2
URL:            https://github.com/gregkh/bti
# kernel.org, not always up to date
Source0:        https://www.kernel.org/pub/software/web/bti/bti-%{version}.tar.xz
# build against the older JSON API available in EPEL6
# new JSON blocked by #903009
Patch0:         bti-034-revert_json_change.patch
Patch1:         bti-034_json-c_013.patch
# fallback, need to run autotools on these
#Source0:        https://github.com/gregkh/bti/archive/%%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  libcurl-devel
# for building from github
%if 0%{?el6}
BuildRequires:  autoconf automake
%endif
# Not using pkgconfig(...) deps yet since we're still supporting EL5
BuildRequires:  pkgconfig
BuildRequires:  liboauth-devel
BuildRequires:  pcre-devel
BuildRequires:  libxml2-devel
BuildRequires:  json-c-devel

%description
Allows you to pipe your bash input to twitter in an easy
and fast manner to annoy the whole world.


%prep
%setup -q
%if 0%{?el6}
%patch0 -p1 -b .revert_json_change
%endif
%if 0%{?fedora} >= 28
%patch1 -p1 -b .json-c_013
%endif

%build
# for building from github
%if 0%{?el6}
autoreconf --install --symlink
%endif
export LDFLAGS="%{?__global_ldflags} -L%{_libdir}/readline5"
%configure
make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT
# bash completion
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/bash_completion.d
cp -p bti-bashcompletion $RPM_BUILD_ROOT%{_sysconfdir}/bash_completion.d/bti


%files
%license COPYING
%doc ChangeLog README RELEASE-NOTES
%doc bti.example
%config(noreplace) %{_sysconfdir}/bash_completion.d/bti
%{_bindir}/bti
%{_bindir}/bti-shrink-urls
%{_mandir}/man1/*



%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 034-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Apr 21 2020 Björn Esser <besser82@fedoraproject.org> - 034-18
- Rebuild (json-c)

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 034-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 034-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 034-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 034-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Mar 06 2018 Björn Esser <besser82@fedoraproject.org> - 034-13
- Rebuilt for libjson-c.so.4 (json-c v0.13.1)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 034-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Dec 10 2017 Björn Esser <besser82@fedoraproject.org> - 034-11
- Rebuilt for libjson-c.so.3

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 034-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 034-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 034-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jul  4 2016 Michel Alexandre Salim <salimma@fedoraproject.org> - 034-7
- Relinquish ownership of `bash_completion.d` (bz#1192801)
- Use license macro

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 034-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 034-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 034-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 034-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Feb 11 2014 Michel Salim <salimma@fedoraproject.org> - 034-2
- Build against older JSON API on EPEL6 (bug #903009)
- Remove references to identi.ca, no longer supported

* Wed Jan 29 2014 Michel Salim <salimma@fedoraproject.org> - 034-1
- Update to 034

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 033-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jul  4 2013 Michel Salim <salimma@fedoraproject.org> - 033-1
- Update to 033 (switches to new Twitter API)
- Spec clean-up: mark EL5-specific sections

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 032-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 032-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jun 19 2012 Michel Salim <salimma@fedoraproject.org> - 032-1
- Update to 032

* Fri Feb 10 2012 Petr Pisar <ppisar@redhat.com> - 031-3
- Rebuild against PCRE 8.30

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 031-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Mar 22 2011 Michel Salim <salimma@fedoraproject.org> - 031-1
- Update to 031

* Sat Mar 19 2011 Michel Salim <salimma@fedoraproject.org> - 030-3
- Improved comment marker fix, now safer and handle lines containing both
  non-marker and marker '#'s

* Fri Mar 18 2011 Michel Salim <salimma@fedoraproject.org> - 030-2
- Improve detection of comment marker in configuration file

* Fri Mar 18 2011 Michel Salim <salimma@fedoraproject.org> - 030-1
- Update to 030

* Sat Mar 12 2011 Michel Salim <salimma@fedoraproject.org> - 029-1
- Update to 029

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 028-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Nov  6 2010 Michel Salim <salimma@fedoraproject.org> - 028-3
- Rebuilt for new libxml2 on Rawhide

* Wed Sep 29 2010 jkeating - 028-2
- Rebuilt for gcc bug 634757

* Wed Sep  8 2010 Michel Salim <salimma@fedoraproject.org> - 028-1
- Update to 028

* Thu May 20 2010 Michel Salim <salimma@fedoraproject.org> - 026-1
- Update to 026

* Wed Aug 19 2009 Michel Salim <salimma@fedoraproject.org> - 023-1
- Update to 023
- Build against readline v5, due to licensing incompatibilities with v6
  (bug #511301)

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 015-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Mar 13 2009 Michel Salim <salimma@fedoraproject.org> - 015-1
- Update to 015

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 014-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Feb 23 2009 Michel Salim <salimma@fedoraproject.org> - 014-1
- Update to 014

* Mon Dec 29 2008 Michel Salim <salimma@fedoraproject.org> - 007-1
- Update to 0.0.7

* Thu Aug 28 2008 Michel Salim <salimma@fedoraproject.org> - 005-1
- Initial package
