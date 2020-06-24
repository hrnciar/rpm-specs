%{?nodejs_find_provides_and_requires}

%global enable_tests 1

Name:           nodejs-concat-stream
Version:        1.6.0
Release:        11%{?dist}
Summary:        Writable stream that concatenates data and calls a callback with the result
License:        MIT
URL:            https://github.com/maxogden/concat-stream
Source0:        https://github.com/maxogden/concat-stream/archive/v%{version}/concat-stream-%{version}.tar.gz
# https://github.com/maxogden/concat-stream/pull/43
Patch0:         nodejs-concat-stream-typedarray.patch
# Fix engines specification in package.json
Patch1:         nodejs-concat-stream-engines.patch
BuildArch:      noarch

%if 0%{?fedora} >= 19
ExclusiveArch:  %{nodejs_arches} noarch
%else
ExclusiveArch:  %{ix86} x86_64 %{arm} noarch
%endif

BuildRequires:  nodejs-packaging

BuildRequires:  npm(tape)
BuildRequires:  npm(inherits)
BuildRequires:  npm(readable-stream)

%description
%{summary}.


%prep
%autosetup -p 1 -n concat-stream-%{version}

%nodejs_fixdep readable-stream '^2.0.5'
%nodejs_fixdep -r typedarray


%build
#nothing to do


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/concat-stream
cp -pr package.json index.js \
    %{buildroot}%{nodejs_sitelib}/concat-stream

%nodejs_symlink_deps


%check
%nodejs_symlink_deps --check
%{__nodejs} -e 'require("./")'
%if 0%{?enable_tests}
/usr/bin/tape test/*.js test/server/*.js
%endif


%files
%doc readme.md
%license LICENSE
%{nodejs_sitelib}/concat-stream


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Aug 16 2019 Tom Hughes <tom@compton.nu> - 1.6.0-10
- Re-enable tests

* Fri Aug 16 2019 Tom Hughes <tom@compton.nu> - 1.6.0-9
- Add patch for invalid package.json

* Fri Aug 16 2019 Tom Hughes <tom@compton.nu> - 1.6.0-8
- Add manual Requires pending nodejs-packaging fix

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed May 31 2017 Jared Smith <jsmith@fedoraproject.org> - 1.6.0-2
- Relax dependency on npm(readable-stream)

* Mon May 08 2017 Jared Smith <jsmith@fedoraproject.org> - 1.6.0-1
- Update to upstream 1.6.0 release

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Jan 17 2016 Tom Hughes <tom@compton.nu> - 1.5.1-1
- Update to 1.5.1 upstream release

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Mar 19 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 1.4.4-2
- add missing BR: npm(inherits)

* Thu Mar 13 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 1.4.4-1
- initial package
