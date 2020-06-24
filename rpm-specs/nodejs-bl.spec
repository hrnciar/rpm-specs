Name:           nodejs-bl
Version:        1.2.2
Release:        3%{?dist}
Summary:        A Node.js Buffer list collector, reader and streamer

License:        MIT
URL:            https://github.com/rvagg/bl
Source0:        https://registry.npmjs.org/bl/-/bl-%{version}.tgz
BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

BuildRequires:  nodejs-packaging

BuildRequires:  npm(tape)
BuildRequires:  npm(hash_file)
BuildRequires:  npm(readable-stream)


%description
bl is a storage object for collections of Node Buffers, exposing them with the 
main Buffer readable API. Also works as a duplex stream so you can collect 
buffers from a stream that emits them and emit buffers to a stream that 
consumes them!


%prep
%autosetup -n package
rm -rf node_

%build


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/bl
cp -pr package.json *.js %{buildroot}%{nodejs_sitelib}/bl
%nodejs_symlink_deps


%check
%nodejs_symlink_deps --check
node test/test.js


%files
%doc README.md
%license LICENSE.md
%{nodejs_sitelib}/bl


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 10 2019 Tom Hughes <tom@compton.nu> - 1.2.2-1
- Update to upstream 1.2.2 release

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Sep 22 2017 Jared Smith <jsmith@fedoraproject.org>
- Update to upstream 1.2.1 release

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Mar 31 2016 Tom Hughes <tom@compton.nu> - 1.1.2-1
- Update to 1.1.2 upstream release

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jul 22 2015 Parag Nemade <pnemade AT fedoraproject DOT org> - 1.0.0-2
- fixdep npm(readable-stream)

* Mon Jul 13 2015 Piotr Popieluch <piotr1212@gmail.com> - 1.0.0-1
- Update to upstream 1.0.0

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Mar  4 2015 Piotr Popieluch <piotr1212@gmail.com> - 0.9.4-1
- Update to upstream 0.9.4

* Mon Dec 22 2014 Piotr Popieluch <piotr1212@gmail.com> - 0.9.3-1
- Initial package
