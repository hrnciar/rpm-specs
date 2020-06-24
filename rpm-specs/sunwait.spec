%global pkgdate 20041208

Name:           sunwait
Summary:        Calculate sunrise, sunset, twilight
Version:        0.1
Release:        0.13.%{pkgdate}%{?dist}
License:        GPLv2+
URL:            http://www.risacher.org/sunwait/
Source0:        http://www.risacher.org/sunwait/sunwait-%{pkgdate}.tar.gz
Source1:        http://www.risacher.org/sunwait/index.html

# patch to include string.h header to avoid warning
Patch0:         sunwait-string.patch

# As of 20-DEC-2014, the source code for the new fork sunwait4windows
# is not being provided in any archive format conducive for packaging,
# so I'm using the author's 2004 release, which still works fine.
# I'll contact Ian Craig, maintainer of the fork, about better source
# release packaging.

# Upstream notified of incorrect-fsf-address by email on 20-DEC-2014
# Requested man page of upstream by email on 25-FEB-2015

BuildRequires:  gcc
%description
Sunwait is a small C program for calculating sunrise and sunset, as
well as civil, nautical, and astronomical twilights. It has features
that make it useful for home automation tasks.

%prep
%setup -q -n %{name}-%{pkgdate}
%patch0 -p1 -b .string
cp -p %{SOURCE1} sunwait.html

%build
make %{?_smp_mflags} CFLAGS="${RPM_OPT_FLAGS}"

%install
install -d -m 755 ${RPM_BUILD_ROOT}/%{_bindir}
install -m 755 sunwait ${RPM_BUILD_ROOT}/%{_bindir}

%files
%license COPYING
%doc sunwait.html
%{_bindir}/sunwait

%changelog
* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.13.20041208
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.12.20041208
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.11.20041208
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.10.20041208
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.9.20041208
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.8.20041208
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.7.20041208
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.6.20041208
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.5.20041208
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-0.4.20041208
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Mar 01 2015 Eric Smith <brouhaha@fedoraproject.org> - 0.1-0.3.20041208
- Made changes for review comments (#1045676 comment 10).

* Thu Feb 26 2015 Eric Smith <brouhaha@fedoraproject.org> - 0.1-0.2.20041208
- Made changes for review comments (#1045676 comment 8).

* Wed Feb 25 2015 Eric Smith <brouhaha@fedoraproject.org> - 0.1-0.1.20041208
- Made changes for review comments (#1045676 comment 4).

* Sat Dec 21 2013 Eric Smith <spacewar@gmail.com> - 20041208-2
- Added missing RPM_OPT_FLAGS.

* Fri Dec 20 2013 Eric Smith <brouhaha@fedoraproject.org> - 20041208-1
- Initial build.
