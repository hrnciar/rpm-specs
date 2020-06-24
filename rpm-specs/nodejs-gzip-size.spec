%{?nodejs_find_provides_and_requires}

%global enable_tests 0
# tests disabled until npm(ava) is packaged in Fedora

Name:       nodejs-gzip-size
Version:    3.0.0
Release:    8%{?dist}
Summary:    Get the gzipped size of a string or buffer
License:    MIT
URL:        https://github.com/sindresorhus/gzip-size
Source0:    http://registry.npmjs.org/gzip-size/-/gzip-size-%{version}.tgz
Source1:    https://raw.githubusercontent.com/sindresorhus/gzip-size/v%{version}/test.js

BuildArch:  noarch
%if 0%{?fedora} >= 19
ExclusiveArch: %{nodejs_arches} noarch
%else
ExclusiveArch: %{ix86} x86_64 %{arm} noarch
%endif

BuildRequires:  nodejs-packaging

%if 0%{?enable_tests}
BuildRequires:  npm(ava)
BuildRequires:  npm(concat-stream)
BuildRequires:  npm(zlib-browserify)
%endif

%description
%{summary}.


%prep
%setup -q -n package
cp -p %{SOURCE1} .


%build
#nothing to do


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/gzip-size
cp -pr package.json index.js \
    %{buildroot}%{nodejs_sitelib}/gzip-size

mkdir -p %{buildroot}%{_bindir}
ln -sf %{nodejs_sitelib}/gzip-size/index.js \
    %{buildroot}%{_bindir}/gzip-size

%nodejs_symlink_deps


%if 0%{?enable_tests}
%check
%nodejs_symlink_deps --check
%__nodejs tap.js
%endif


%files
%{!?_licensedir:%global license %doc}
%doc *.md
%license license
%{nodejs_sitelib}/gzip-size
%{_bindir}/gzip-size


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jul 07 2016 Jared Smith <jsmith@fedoraproject.org> - 3.0.0-1
- Update to upstream 3.0.0 release

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Mar 13 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.1.0-1
- initial package
