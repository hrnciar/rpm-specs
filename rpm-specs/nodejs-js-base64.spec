# This macro is needed at the start for building on EL6
%{?nodejs_find_provides_and_requires}

%global enable_tests 0

%global barename js-base64

Name:               nodejs-js-base64
Version:            2.1.7
Release:            12%{?dist}
Summary:            Yet another Base64 transcoder in pure-JS

License:            BSD
URL:                https://www.npmjs.org/package/js-base64
Source0:            http://registry.npmjs.org/%{barename}/-/%{barename}-%{version}.tgz

# The license actually BSD https://github.com/dankogai/js-base64/issues/18
Source1:            https://raw.githubusercontent.com/dankogai/js-base64/master/LICENSE.md

BuildArch:          noarch
%if 0%{?fedora} >= 19
ExclusiveArch:      %{nodejs_arches} noarch
%else
ExclusiveArch:      %{ix86} x86_64 %{arm} noarch
%endif

BuildRequires:      nodejs-packaging >= 6


%if 0%{?enable_tests}
BuildRequires:      npm(mocha)
%endif

%description
Yet another Base64 transcoder

%prep
%setup -q -n package

# Copy our Fedora-shipped license file in
cp -pr %{SOURCE1} .

# Remove bundled node_modules if there are any..
rm -rf node_modules/

%nodejs_fixdep --caret

%build
%nodejs_symlink_deps --build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/js-base64
cp -pr package.json base64.js \
    %{buildroot}%{nodejs_sitelib}/js-base64

%nodejs_symlink_deps

%check
%if 0%{?enable_tests}
%nodejs_symlink_deps --check
mocha
%endif

%files
%doc README.md
%license LICENSE.md
%{nodejs_sitelib}/js-base64/

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.7-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.7-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.7-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.7-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Sep 14 2015 Ralph Bean <rbean@redhat.com> - 2.1.7-3
- Replace our LICENSE-MIT with the new correct license from usptream
  https://github.com/dankogai/js-base64/issues/18

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Feb 18 2015 Ralph Bean <rbean@redhat.com> - 2.1.7-1
- new version

* Tue Sep 02 2014 Ralph Bean <rbean@redhat.com> - 2.1.5-2
- Relicense to MIT
- Ship our own LICENSE-MIT file.

* Mon Aug 18 2014 Ralph Bean <rbean@redhat.com> - 2.1.5-1
- Initial packaging for Fedora.
