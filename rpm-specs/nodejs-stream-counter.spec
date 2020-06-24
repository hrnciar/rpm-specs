%{?nodejs_find_provides_and_requires}

%global enable_tests 1

Name:       nodejs-stream-counter
Version:    0.2.0
Release:    12%{?dist}
Summary:    Keeps track of how many bytes have been written to a stream
License:    BSD
URL:        https://github.com/superjoe30/node-stream-counter
Source0:    http://registry.npmjs.org/stream-counter/-/stream-counter-%{version}.tgz
# Upstream have relicensed to MIT upstream, but this release remains under
# BSD license. Include a copy to comply with license requirements.
Source10:   LICENSE

# Use Node.js core instead of the forked npm(readable-stream)
Patch0:     %{name}-0.2.0-Use-Node.js-core.patch

BuildArch:  noarch
%if 0%{?fedora} >= 19
ExclusiveArch: %{nodejs_arches} noarch
%else
ExclusiveArch: %{ix86} x86_64 %{arm} noarch
%endif

BuildRequires:  nodejs-packaging

%description
%{summary}.


%prep
%setup -q -n package
%patch0 -p1
%nodejs_fixdep -r readable-stream
cp -a %{SOURCE10} .


%build
#nothing to do


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/stream-counter
cp -pr package.json index.js \
    %{buildroot}%{nodejs_sitelib}/stream-counter

%nodejs_symlink_deps


%if 0%{?enable_tests}
%check
%nodejs_symlink_deps --check
%__nodejs test/test.js
%endif


%files
%doc LICENSE README.md
%{nodejs_sitelib}/stream-counter


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Apr 20 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.2.0-2
- amend license

* Sun Mar 02 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.2.0-1
- initial package
