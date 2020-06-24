%{?nodejs_find_provides_and_requires}

%global enable_tests 1

Name:       nodejs-zlib-browserify
Version:    0.0.3
Release:    11%{?dist}
Summary:    Wrapper for zlib.js to allow for use in browsers
License:    MIT
URL:        https://github.com/brianloveswords/zlib-browserify
Source0:    http://registry.npmjs.org/zlib-browserify/-/zlib-browserify-%{version}.tgz

# Use npm(zlibjs) instead of bundled zlib.js.
# https://github.com/brianloveswords/zlib-browserify/pull/11
Patch0:     %{name}-0.0.3-Use-zlibjs-module.patch

BuildArch:  noarch
ExclusiveArch: %{nodejs_arches} noarch

BuildRequires:  nodejs-packaging

%if 0%{?enable_tests}
BuildRequires:  npm(tap)
BuildRequires:  npm(tape)
BuildRequires:  npm(zlibjs)
%endif

%description
%{summary}.


%prep
%setup -q -n package
%patch0 -p1
# This module is not required for runtime.
%nodejs_fixdep -r tape


%build
#nothing to do


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/zlib-browserify
cp -pr package.json index.js \
    %{buildroot}%{nodejs_sitelib}/zlib-browserify

%nodejs_symlink_deps


%if 0%{?enable_tests}
%check
%nodejs_symlink_deps --check
%tap test/*.test.js
%endif


%files
%doc LICENSE readme.md
%{nodejs_sitelib}/zlib-browserify


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Mar 13 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.0.3-1
- update to upstream release 0.0.3
- patch to use npm(zlibjs) module

* Fri Jun 21 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.0.1-1
- initial package
