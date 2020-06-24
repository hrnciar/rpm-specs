# Generated from fog-libvirt-0.0.1.gem by gem2rpm -*- rpm-spec -*-
%global gem_name fog-libvirt

Name: rubygem-%{gem_name}
Version: 0.7.0
Release: 1%{?dist}
Summary: Module for the 'fog' gem to support libvirt
License: MIT
URL: http://github.com/fog/fog-libvirt
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildRequires: %{_bindir}/shindo
BuildRequires: rubygem(ruby-libvirt)
BuildRequires: rubygem(minitest)
BuildRequires: rubygem(mocha) => 1.1.0
BuildRequires: rubygem(fog-core)
BuildRequires: rubygem(fog-xml)
BuildRequires: rubygem(fog-json)
BuildArch: noarch

%description
This library can be used as a module for 'fog' or as standalone libvirt
provider.


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -n %{gem_name}-%{version}

%build
gem build ../%{gem_name}-%{version}.gemspec
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

# Run the test suite
%check
pushd .%{gem_instdir}
FOG_MOCK=true shindo -Ilib tests
ruby -Iminitests -e "Dir.glob './minitests/**/*_test.rb', &method(:require)"
popd

%files
%dir %{gem_instdir}
%license %{gem_instdir}/LICENSE.md
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CONTRIBUTORS.md
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/fog-libvirt.gemspec
%{gem_instdir}/tests
%{gem_instdir}/minitests

%changelog
* Mon Feb 17 2020 Pavel Valena <pvalena@redhat.com> - 0.7.0-1
- Update to fog-libvirt 0.7.0.

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Nov 01 2018 Vít Ondruch <vondruch@redhat.com> - 0.5.0-2
- Relax fog-core dependency.

* Wed Aug 15 2018 Pavel Valena <pvalena@redhat.com> - 0.5.0-1
- Update to fog-libvirt 0.5.0.

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Nov 21 2017 Pavel Valena <pvalena@redhat.com> - 0.4.2-1
- Update to 0.4.2.

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Sep 26 2016 Vít Ondruch <vondruch@redhat.com> - 0.3.0-1
- Update to fog-libvirt 0.3.0.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 24 2015 Josef Stribny <jstribny@redhat.com> - 0.0.3-1
- Update to 0.0.3

* Mon Sep 14 2015 Josef Stribny <jstribny@redhat.com> - 0.0.2-2
- Drop libvirt requirement, it should be pulled in via ruby-libvirt

* Mon Jun 29 2015 Josef Stribny <jstribny@redhat.com> - 0.0.2-1
- Update to 0.0.2

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 05 2015 Josef Stribny <jstribny@redhat.com> - 0.0.1-1
- Initial package
