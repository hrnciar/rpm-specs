# Test deps: npm(referee) and npm(sinon) not yet in Fedora
%global enable_tests 0
%global srcname lolex

Name:           nodejs-%{srcname}
Version:        1.3.2
Release:        9%{?dist}
Summary:        Fake JavaScript timers
License:        BSD
URL:            https://github.com/sinonjs/lolex
Source0:        https://registry.npmjs.org/%{srcname}/-/%{srcname}-%{version}.tgz

BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

BuildRequires:  nodejs-packaging

%if 0%{?enable_tests}
BuildRequires:  npm(referee)
BuildRequires:  npm(sinon)
%endif


%description
JavaScript implementation of the timer APIs; setTimeout, clearTimeout, 
setImmediate, clearImmediate, setInterval, clearInterval, and 
requestAnimationFrame, along with a clock instance that controls the flow of 
time. Lolex also provides a Date implementation that gets its time from the 
clock.


%prep
%setup -q -n package


%build
#nothing to do


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{srcname}
cp -pr package.json src/ \
    %{buildroot}%{nodejs_sitelib}/%{srcname}

%nodejs_symlink_deps


%if 0%{?enable_tests}
%check
%nodejs_symlink_deps --check
npm run test-node
%endif


%files
%doc Readme.md
%license LICENSE
%{nodejs_sitelib}/%{srcname}


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Oct 13 2015 Piotr Popieluch <piotr1212@gmail.com> - 1.3.2-1
- update to 1.3.2

* Tue Sep 01 2015 Piotr Popieluch <piotr1212@gmail.com> - 1.3.1-2
- remove toplevel lolex.js
- remove tests from rpm
- update test for only testing Node.js part

* Sat Aug 29 2015 Piotr Popieluch <piotr1212@gmail.com> - 1.3.1-1
- update to latest upstream

* Fri Jan 02 2015 Piotr Popieluch <piotr1212@gmail.com> - 1.2.0-1
- update to latest upstream

* Tue Nov 18 2014 Piotr Popieluch <piotr1212@gmail.com> - 1.1.0-1
- Initial package
