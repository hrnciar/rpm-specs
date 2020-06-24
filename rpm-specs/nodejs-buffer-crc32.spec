%{?nodejs_find_provides_and_requires}

%global enable_tests 0

Name:       nodejs-buffer-crc32
Version:    0.2.1
Release:    17%{?dist}
Summary:    A pure JavaScript CRC32 algorithm that plays nice with binary data
License:    MIT
URL:        https://github.com/brianloveswords/buffer-crc32
Source0:    http://registry.npmjs.org/buffer-crc32/-/buffer-crc32-%{version}.tgz
# License is now in upstream repository:
# https://github.com/brianloveswords/buffer-crc32/commit/1b7489d304
Source20:   LICENSE

BuildArch:  noarch
%if 0%{?fedora} >= 19
ExclusiveArch: %{nodejs_arches} noarch
%else
ExclusiveArch: %{ix86} x86_64 %{arm} noarch
%endif

BuildRequires:  nodejs-packaging

%if 0%{?enable_tests}
BuildRequires:  npm(tap)
%endif

%description
This Node.js module provides a pure JavaScript CRC32 algorithm that works
with binary data and fancy character sets, output buffers, signed or unsigned
data and also has tests.

It is derived from the sample CRC implementation in the PNG specification:
http://www.w3.org/TR/PNG/#D-CRCAppendix


%prep
%setup -q -n package
cp -p %{SOURCE20} .


%build
#nothing to do


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/buffer-crc32
cp -pr package.json index.js \
    %{buildroot}%{nodejs_sitelib}/buffer-crc32

%nodejs_symlink_deps


%if 0%{?enable_tests}
%check
%tap tests/*.test.js
%endif


%files
%doc LICENSE README.md
%{nodejs_sitelib}/buffer-crc32


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jul 06 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.2.1-6
- fix compatible arches on f18/el6

* Fri Jul 05 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.2.1-5
- restrict to compatible arches

* Wed Jun 19 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.2.1-4
- rebuild for missing npm(buffer-crc32) provides on EL6

* Fri Feb 22 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.2.1-3
- add a copy of the MIT license while waiting for the next release

* Tue Feb 12 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.2.1-2
- correct various spellings
- add comment that license is now in upstream git

* Mon Feb 11 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.2.1-1
- initial package
