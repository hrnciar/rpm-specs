Name:           nodejs-isstream
Version:        0.1.2
Release:        11%{?dist}

Summary:        Determine if an object is a Stream
License:        MIT
URL:            https://github.com/rvagg/isstream
Source0:        https://registry.npmjs.org/isstream/-/isstream-%{version}.tgz
BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

BuildRequires:  nodejs-packaging

BuildRequires:  npm(tape)
BuildRequires:  npm(core-util-is)
BuildRequires:  npm(isarray)
BuildRequires:  npm(string_decoder)
BuildRequires:  npm(inherits)
# Package ships with two bundled versions of readable-stream for tests.
# We are only interested in testing against the version which is actually in
# Fedora.
BuildRequires:  npm(readable-stream)

%description
%{summary}.


%prep
%autosetup -n package
%nodejs_fixdep --dev readable-stream
rm -rf node_modules


%build



%install
mkdir -p %{buildroot}%{nodejs_sitelib}/isstream
cp -pr package.json isstream.js %{buildroot}%{nodejs_sitelib}/isstream
%nodejs_symlink_deps

%check
%nodejs_symlink_deps --check
# extra symlinks so we use Fedora shipped readable-stream
ln -s ./node_modules/readable-stream readable-stream-1.0
ln -s ./node_modules/readable-stream readable-stream-1.1
%__nodejs test.js


%files
%doc README.md
%license LICENSE.md
%{nodejs_sitelib}/isstream


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 10 2019 Tom Hughes <tom@compton.nu> - 0.1.2-9
- Resurrect retired package

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Nov 06 2015 Piotr Popieluch <piotr1212@gmail.com> - 0.1.2-2
- Add readable-stream to BR and symlinks and enable tests

* Sat Oct 24 2015 Piotr Popieluch <piotr1212@gmail.com> - 0.1.2-1
- Initial package
