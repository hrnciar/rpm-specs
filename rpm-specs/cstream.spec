Summary:   General-purpose stream-handling tool
Name:      cstream
Version:   3.1.1
Release:   15%{?dist}

License:   MIT
URL:       http://www.cons.org/cracauer/cstream.html
Source:    http://www.cons.org/cracauer/download/%{name}-%{version}.tar.gz
Patch2:    %{name}-%{version}-Wextra.patch
Patch3:    %{name}-%{version}-double-assignment.patch
Patch5:    %{name}-%{version}-meh.patch
Patch6:    %{name}-%{version}-Werror=tautological-compare.patch



BuildRequires:  gcc
%description
cstream filters data streams, much like the UNIX tool dd(1).

It has a more traditional commandline syntax, support for precise
bandwidth limiting and reporting and support for FIFOs.

Data limits and throughput rate calculation will work for files > 4 GB.


%prep
%setup -q
%patch2 -p1 -b .Wextra
%patch3 -p1 -b .double-assignment
%patch5 -p1 -b .meh
%patch6 -p1 -b .Werror=autological-compare


%build
%{configure} INSTALL="%{__install} -p"
%{__make} %{?_smp_mflags} CFLAGS="%{optflags} -Wall -Wextra -Wno-unused-parameter -Werror"


%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"



%check
%{__make} check installcheck DESTDIR="%{buildroot}"


%files
%doc CHANGES COPYRIGHT README TODO
%doc %{_mandir}/man1/cstream.1*
%{_bindir}/cstream


%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon May 16 2016 Hans Ulrich Niedermann <hun@n-dimensional.de> - 3.1.1-7
- remove useless %%defattr for clarity

* Mon May 16 2016 Hans Ulrich Niedermann <hun@n-dimensional.de> - 3.1.1-6
- Fix FTBFS due to -Werror=tautological-compare (#1307412)

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Nov 16 2013 Hans Ulrich Niedermann <hun@n-dimensional.de> - 3.1.1-1
- Update to cstream-3.1.1 (#903580)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Sep 12 2011 Hans Ulrich Niedermann <hun@n-dimensional.de> - 3.0.0-1
- Update to cstream-3.0.0 (IPv6 and small fixes)

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Sep 10 2010 Hans Ulrich Niedermann <hun@n-dimensional.de> - 2.7.6-4
- Remove double variable assignment (#631150)

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Dec 20 2008 Hans Ulrich Niedermann <hun@n-dimensional.de> - 2.7.6-1
- Update to upstream's 2.7.6 release.

* Sat Feb 09 2008 Hans Ulrich Niedermann <hun@n-dimensional.de> - 2.7.5-1
- Update to upstream's 2.7.5 release.

* Sat Feb 09 2008 Hans Ulrich Niedermann <hun@n-dimensional.de> - 2.7.4-4
- Add %%{?dist} to Release:

* Fri Feb 08 2008 Hans Ulrich Niedermann <hun@n-dimensional.de> - 2.7.4-3
- More compile warnings (-Wall -Wextra -Werror).
- Redacted description down to the most important points.

* Fri Feb 08 2008 Hans Ulrich Niedermann <hun@n-dimensional.de> - 2.7.4-2
- Spec file cleanups (use install target, get rpmlint to shut up).

* Fri Feb 08 2008 Mike Weisenborn <mike@weisenborn.com> - 2.7.4-1
- Initial package
