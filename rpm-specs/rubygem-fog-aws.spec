# Generated from fog-aws-0.1.1.gem by gem2rpm -*- rpm-spec -*-
%global gem_name fog-aws

Name: rubygem-%{gem_name}
Version: 3.3.0
Release: 5%{?dist}
Summary: Module for the 'fog' gem to support Amazon Web Services
License: MIT
URL: https://github.com/fog/fog-aws
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# The test suite fails when tests/requests/sts/assume_role_with_web_identity_tests.rb
# is executed prior tests/models/iam/roles_tests.rb
# https://github.com/fog/fog-aws/issues/491
Patch0: rubygem-fog-aws-3.3.0-cleanup-roles-in-sts-test.patch
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildRequires: rubygem(fog-xml)
BuildRequires: rubygem(fog-json)
BuildRequires: rubygem(ipaddress)
BuildRequires: rubygem(rubyzip)
BuildRequires: %{_bindir}/shindo
BuildArch: noarch

%description
This library can be used as a module for `fog` or as standalone provider
to use the Amazon Web Services in applications.


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -n %{gem_name}-%{version}

%patch0 -p1

%build
# Create the gem as gem install only works on a gem file
gem build ../%{gem_name}-%{version}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/



%check
pushd .%{gem_instdir}
# Don't use Bundler.
sed -i '/Bundler/ s/^/#/' tests/helper.rb

# The file is not autoloaded for some reason.
# https://github.com/fog/fog-aws/issues/301
sed -i "1i require 'fog/aws/requests/dns/change_resource_record_sets'\n" \
  tests/requests/dns/change_resource_record_sets_tests.rb

FOG_MOCK=true shindont
popd

%files
%dir %{gem_instdir}
%exclude %{gem_instdir}/.*
%license %{gem_instdir}/LICENSE.md
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/CONTRIBUTING.md
%doc %{gem_instdir}/CONTRIBUTORS.md
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/fog-aws.gemspec
%{gem_instdir}/gemfiles
%{gem_instdir}/stale.yml
%{gem_instdir}/tests

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Nov 02 2018 Vít Ondruch <vondruch@redhat.com> - 3.3.0-1
- Update to fog-aws 3.3.0.

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Feb 22 2017 Vít Ondruch <vondruch@redhat.com> - 1.2.0-1
- Update to fog-aws 1.2.0.

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Sep 26 2016 Vít Ondruch <vondruch@redhat.com> - 0.12.0-1
- Update to fog-aws 0.12.0.

* Tue Sep 06 2016 Vít Ondruch <vondruch@redhat.com> - 0.11.0-1
- Update to fog-aws 0.11.0.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Nov 20 2015 Vít Ondruch <vondruch@redhat.com> - 0.7.6-1
- Update to fog-aws 0.7.6.

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Mar 10 2015 Vít Ondruch <vondruch@redhat.com> - 0.1.1-1
- Initial package
