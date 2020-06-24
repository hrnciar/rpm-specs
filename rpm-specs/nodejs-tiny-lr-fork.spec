%{?nodejs_find_provides_and_requires}

# This is a fork of the original tiny-lr: <https://github.com/mklabs/tiny-lr>.
# The maintainer of the fork has stated that the fork is only temporary and
# will cease to exist once the maintainer of the original software springs
# back to life. The fork has gained favour among other modules, notably the
# Grunt project, so we will ship the fork with the intention of Obsoleting it
# once the original tiny-lr has been revived.

# Versions of connect and express used in the test suite are outdated.
%global enable_tests 0

Name:       nodejs-tiny-lr-fork
Version:    0.0.5
Release:    15%{?dist}
Summary:    A tiny LiveReload server implementation you can spawn in the background
License:    MIT
URL:        https://github.com/shama/tiny-lr
Source0:    https://registry.npmjs.org/tiny-lr-fork/-/tiny-lr-fork-%{version}.tgz

BuildArch:  noarch
%if 0%{?fedora} >= 19
ExclusiveArch: %{nodejs_arches} noarch
%else
ExclusiveArch: %{ix86} x86_64 %{arm} noarch
%endif

BuildRequires:  nodejs-packaging

%if 0%{?enable_tests}
BuildRequires:  npm(connect)
BuildRequires:  npm(debug)
BuildRequires:  npm(express)
BuildRequires:  npm(faye-websocket)
BuildRequires:  npm(mocha)
BuildRequires:  npm(noptify)
BuildRequires:  npm(qs)
BuildRequires:  npm(request)
BuildRequires:  npm(supertest)
%endif

%description
%{summary}.


%prep
%setup -q -n package

%nodejs_fixdep faye-websocket '~0.7'
%nodejs_fixdep qs '^6.0.2'
%nodejs_fixdep noptify '~0.0.3'
%nodejs_fixdep debug '^2.2.0'


%build
#nothing to do


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/tiny-lr-fork
cp -pr package.json lib/ tasks/ \
    %{buildroot}%{nodejs_sitelib}/tiny-lr-fork

mkdir -p %{buildroot}%{nodejs_sitelib}/tiny-lr-fork/bin
install -p -m755 bin/tiny-lr \
    %{buildroot}%{nodejs_sitelib}/tiny-lr-fork/bin/tiny-lr
install -p -m755 bin/update-livereload \
    %{buildroot}%{nodejs_sitelib}/tiny-lr-fork/bin/update-livereload

mkdir -p %{buildroot}%{_bindir}
ln -sf %{nodejs_sitelib}/tiny-lr-fork/bin/tiny-lr \
    %{buildroot}%{_bindir}/tiny-lr
ln -sf %{nodejs_sitelib}/tiny-lr-fork/bin/update-livereload \
    %{buildroot}%{_bindir}/update-livereload

%nodejs_symlink_deps


%if 0%{?enable_tests}
%check
%nodejs_symlink_deps --check
/usr/bin/mocha --reporter spec
%endif


%files
%doc readme.md
%license LICENSE-MIT
%{nodejs_sitelib}/tiny-lr-fork
%{_bindir}/tiny-lr
%{_bindir}/update-livereload


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.5-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.5-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.5-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jan 20 2016 Tom Hughes <tom@compton.nu> - 0.0.5-7
- Update npm(qs) dependency

* Tue Nov 24 2015 Tom Hughes <tom@compton.nu> - 0.0.5-6
- update npm(debug) dependency

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Apr 20 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.0.5-3
- fix versioned dependencies

* Sun Mar 30 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.0.5-2
- symlink to _bindir

* Sat Mar 29 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.0.5-1
- initial package
