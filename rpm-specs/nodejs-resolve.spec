%{?nodejs_find_provides_and_requires}

# Disable tests due to the way errors are now thrown
%global enable_tests 0

Name:           nodejs-resolve
Version:        1.7.1
Release:        5%{?dist}
Summary:        Resolve like require.resolve() on behalf of files asynchronously/synchronously

License:        MIT
URL:            https://github.com/substack/node-resolve
Source0:        https://registry.npmjs.org/resolve/-/resolve-%{version}.tgz
BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

BuildRequires:  nodejs-packaging

%if 0%{?enable_tests}
BuildRequires:  npm(tap)
BuildRequires:  npm(tape)
%endif

%description
%{summary}.


%prep
%setup -q -n package


%build
#nothing to do


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/resolve
cp -pr package.json index.js lib/ \
    %{buildroot}%{nodejs_sitelib}/resolve

%nodejs_symlink_deps


%check
%nodejs_symlink_deps --check
%__nodejs -e "require('./')"
%if 0%{?enable_tests}
%tap test/*.js
%endif


%files
%{!?_licensedir:%global license %doc}
%doc readme.markdown example/
%license LICENSE
%{nodejs_sitelib}/resolve


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu May 31 2018 Jared K. Smith <jsmith@fedoraproject.org> - 1.7.1-1
- Update to upstream 1.7.1 release

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Mar  7 2016 Tom Hughes <tom@compton.nu> - 1.1.7-1
- Update to 1.1.7 upstream release

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan  8 2016 Tom Hughes <tom@compton.nu> - 1.1.6-1
- Update to 1.1.6 upstream release

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Sep 03 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.5.0-1
- update to upstream release 0.5.0

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jul 11 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.4.0-2
- add ExclusiveArch logic

* Fri Jun 21 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.4.0-1
- initial package
