# This macro is needed at the start for building on EL6
%{?nodejs_find_provides_and_requires}

%global barename supports-color
%global enable_tests 0
# tests disabled until such time as 'ava' is packaged in Fedora


Name:               nodejs-supports-color
Version:            4.4.0
Release:            6%{?dist}
Summary:            Detect whether a terminal supports color

License:            MIT
URL:                https://github.com/chalk/supports-color
Source0:            http://registry.npmjs.org/%{barename}/-/%{barename}-%{version}.tgz

# 4.4.0 release hasn't been tagged in github yet
#Source1:            https://raw.githubusercontent.com/chalk/supports-color/v%{version}/test.js
Source1:            https://raw.githubusercontent.com/chalk/supports-color/master/test.js

BuildArch:          noarch
%if 0%{?fedora} >= 19
ExclusiveArch:      %{nodejs_arches} noarch
%else
ExclusiveArch:      %{ix86} x86_64 %{arm} noarch
%endif

BuildRequires:      nodejs-packaging >= 6
BuildRequires:      npm(has-flag)

%if 0%{?enable_tests}
BuildRequires:      npm(require-uncached)
BuildRequires:      npm(mocha)
%endif


%description
Detect whether a terminal supports color

%prep
%setup -q -n package
cp %{SOURCE1} .

# Remove bundled node_modules if there are any..
rm -rf node_modules/

%nodejs_fixdep --caret

%build
# This causes warnings when running the tests
#%nodejs_symlink_deps --build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/supports-color
cp -pr package.json *.js \
    %{buildroot}%{nodejs_sitelib}/supports-color

mkdir -p %{buildroot}/%{_bindir}/
ln -s %{nodejs_sitelib}/supports-color/cli.js \
    %{buildroot}/%{_bindir}/supports-color

%nodejs_symlink_deps

%check
%nodejs_symlink_deps --check
%{__nodejs} -e 'require("./")'
%if 0%{?enable_tests}
%{_bindir}/mocha -R spec
%else
%{_bindir}/echo -e "\e[101m -=#=- Tests disabled -=#=- \e[0m"
%endif

%files
%{!?_licensedir:%global license %doc}
%license license
%doc readme.md
%{nodejs_sitelib}/supports-color/
%{_bindir}/supports-color

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Sep 20 2017 Jared Smith <jsmith@fedoraproject.org> - 4.4.0-1
- Update to upstream 4.4.0 release

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Feb 10 2015 Ralph Bean <rbean@redhat.com> - 1.2.0-2
- Include license from github.
- Enable tests.
- Make cli.js into a symlink.
- Comment out nodejs_symlink_deps --build, as per review.

* Tue Dec 02 2014 Ralph Bean <rbean@redhat.com> - 1.2.0-1
- Initial packaging for Fedora.
