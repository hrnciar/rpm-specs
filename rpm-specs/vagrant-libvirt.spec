%global vagrant_plugin_name vagrant-libvirt

%global vagrant_spec_commit 94a9d31ba18b4130b14da12a2f7b4001c3d2ff12

Name: %{vagrant_plugin_name}
Version: 0.0.45
Release: 4%{?dist}
Summary: libvirt provider for Vagrant
License: MIT
URL: https://github.com/vagrant-libvirt/vagrant-libvirt
Source0: https://rubygems.org/gems/%{vagrant_plugin_name}-%{version}.gem
# The library has no official release yet. But since it is just test
# dependency, it should be fine to include the source right here.
# wget https://github.com/mitchellh/vagrant-spec/archive/9bba7e1228379c0a249a06ce76ba8ea7d276afb/vagrant-spec-f1a18fd3e5387328ca83e016e48373aadb67112a.tar.gz
Source2: https://github.com/mitchellh/vagrant-spec/archive/%{vagrant_spec_commit}/vagrant-spec-%{vagrant_spec_commit}.tar.gz
# Enable QEMU Session by default
# https://github.com/vagrant-libvirt/vagrant-libvirt/pull/969
Patch0: vagrant-libvirt-0.0.45-enable-qemu-session-by-default.patch
# Allow customizing of virt-sysprep behaviour on package.
# Backport of https://github.com/vagrant-libvirt/vagrant-libvirt/commit/deb36bef8b6c0b696ea0045563fb5cc0e4895f73.
Patch1: 0001-Allow-customizing-of-virt-sysprep-behaviour-on-packa.patch
# Use fetch to obtain environment variable value in package_domain.
# Backport of https://github.com/vagrant-libvirt/vagrant-libvirt/commit/f8eae9984d7f9f0bcc83fa3082592968487c0fb2.
Patch2: 0002-Use-fetch-to-obtain-environment-variable-value-in-pa.patch
# Halt a domain before packaging it as a box to avoid hard to debug issues.
# https://github.com/vagrant-libvirt/vagrant-libvirt/pull/1034.
Patch3: 0003-Halt-a-domain-before-packaging-it-as-a-box.patch

Requires: ruby(release)
Requires: ruby(rubygems)
Requires: rubygem(fog-libvirt) >= 0.3.0
Requires: rubygem(nokogiri) >= 1.6
# Vagrant changed packaging scriptlets in version 1.9.1.
Requires: vagrant >= 1.9.1
# Required by "vagrant package" command (rhbz#1292217).
Recommends: %{_bindir}/virt-sysprep
BuildRequires: vagrant >= 1.9.1
BuildRequires: rubygem(bundler)
BuildRequires: rubygem(rdoc)
BuildRequires: rubygem(rspec)
BuildRequires: rubygem(fog-libvirt)
BuildRequires: rubygem(thor)
BuildRequires: rubygems-devel
BuildArch: noarch
Provides: vagrant(%{vagrant_plugin_name}) = %{version}

%description
libvirt provider for Vagrant.


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -n %{vagrant_plugin_name}-%{version} -b 2

%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

# Relax fog-core dependency to work with recently rebased one
%gemspec_remove_dep -s ../%{vagrant_plugin_name}-%{version}.gemspec -g fog-core '~> 1.43.0'
%gemspec_add_dep -s ../%{vagrant_plugin_name}-%{version}.gemspec -g fog-core '>= 1.43.0'

%build
gem build ../%{vagrant_plugin_name}-%{version}.gemspec
%vagrant_plugin_install

%install
mkdir -p %{buildroot}%{vagrant_plugin_dir}
cp -a .%{vagrant_plugin_dir}/* \
        %{buildroot}%{vagrant_plugin_dir}/

%check
# Edit gemspec of vagrant-spec
pushd ../vagrant-spec-%{vagrant_spec_commit}
# Remove the git reference, which is useless in our case.
sed -i '/git/ s/^/#/' vagrant-spec.gemspec

# Relax the Childprocess dependency, since Fedora currently ships with different version
# https://src.fedoraproject.org/rpms/rubygem-childprocess/pull-request/1
%gemspec_remove_dep -s vagrant-spec.gemspec -g childprocess '~> 0.6.0'
%gemspec_add_dep -s vagrant-spec.gemspec -g childprocess '>= 0.5.0'

# Relax the dependencies, since Fedora ships with newer versions.
sed -i '/thor/ s/~>/>=/' vagrant-spec.gemspec
sed -i '/rspec/ s/~>/>=/' vagrant-spec.gemspec
popd

# Use actual gemspec for tests
cp ../%{vagrant_plugin_name}-%{version}.gemspec .%{vagrant_plugin_instdir}/%{vagrant_plugin_name}.gemspec

pushd .%{vagrant_plugin_instdir}
# Create dummy Gemfile and load dependencies via gemspec file
echo "gem 'vagrant'" > Gemfile
echo "gem 'rdoc'" >> Gemfile
echo "gem 'vagrant-spec', :path => '%{_builddir}/vagrant-spec-%{vagrant_spec_commit}'" >> Gemfile
echo "gemspec" >> Gemfile

# We don't care about code coverage.
sed -i '/[cC]overalls/ s/^/#/' spec/spec_helper.rb

# Relax developement rspec dependency
sed -i '/rspec/ s/~>/>=/' %{vagrant_plugin_name}.gemspec

GEM_PATH=%{vagrant_plugin_dir}:`ruby -e "print Gem.path.join(':')"` bundle exec rspec spec
popd

%files
%dir %{vagrant_plugin_instdir}
%exclude %{vagrant_plugin_instdir}/.*
%license %{vagrant_plugin_instdir}/LICENSE
%{vagrant_plugin_libdir}
%{vagrant_plugin_instdir}/locales
%{vagrant_plugin_instdir}/tools
%exclude %{vagrant_plugin_cache}
%{vagrant_plugin_spec}

%files doc
%doc %{vagrant_plugin_docdir}
%doc %{vagrant_plugin_instdir}/example_box
%{vagrant_plugin_instdir}/Gemfile
%doc %{vagrant_plugin_instdir}/README.md
%{vagrant_plugin_instdir}/Rakefile
%{vagrant_plugin_instdir}/spec
%{vagrant_plugin_instdir}/vagrant-libvirt.gemspec

%changelog
* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.45-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Sep 08 2019 Tadej Janež <tadej.j@nez.si> - 0.0.45-3
- Backport/Add useful features and fixes from upstream:
  - Allow customizing of virt-sysprep behaviour on package.
  - Use fetch to obtain environment variable value in package_domain.
  - Halt a domain before packaging it as a box to avoid hard to debug issues.

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.45-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Feb 14 2019 Pavel Valena <pvalena@redhat.com> - 0.0.45-1
- Update to vagrant-libvirt 0.0.45.
- Enable QEMU Session by default

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.43-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Nov 02 2018 Pavel Valena <pvalena@redhat.com> - 0.0.43-2
- Relax fog-core dependency to work with recently rebased one.

* Mon Oct 01 2018 pvalena <pvalena@redhat.com> - 0.0.43-1
- Update to vagrant-libvirt 0.0.43.

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.40-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.40-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Dec 08 2017 Pavel Valena <pvalena@redhat.com> - 0.0.40-3
- Fix invalid XML creation on custom domain name (rhbz#1518899).

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.40-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 19 2017 Vít Ondruch <vondruch@redhat.com> - 0.0.40-1
- Update to vagrant-libvirt 0.0.40.

* Fri Feb 24 2017 Vít Ondruch <vondruch@redhat.com> - 0.0.37-4
- Fix Vagrant error when network is specified (rhbz#1426565).

* Mon Feb 13 2017 Vít Ondruch <vondruch@redhat.com> - 0.0.37-3
- Fix compatiblity with Vagrant 1.9.1.

* Mon Feb 06 2017 Vít Ondruch <vondruch@redhat.com> - 0.0.37-2
- Use file dependency rather then package dependency.

* Wed Feb 01 2017 Vít Ondruch <vondruch@redhat.com> - 0.0.37-1
- Update to vagrant-libvirt 0.0.37.
- Recommends libguestfs required by "vagrant package" (rhbz#1292217).

* Thu Jan 05 2017 Vít Ondruch <vondruch@redhat.com> - 0.0.36-2
- Fix compatibility with latest Bundler (rhbz#1409381).

* Sun Jan  1 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.0.36-2
- Relax nokogiri dependency

* Mon Oct 10 2016 Vít Ondruch <vondruch@redhat.com> - 0.0.36-1
- Update to vagrant-libvirt 0.0.36.

* Tue Oct 04 2016 Vít Ondruch <vondruch@redhat.com> - 0.0.35-1
- Update to vagrant-libvirt 0.0.35.

* Wed Aug 03 2016 Vít Ondruch <vondruch@redhat.com> - 0.0.33-1
- Update to vagrant-libvirt 0.0.33.
- Drop the polkit rules. Use libvirt group instead.

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.32-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Oct 14 2015 Josef Stribny <jstribny@redhat.com> - 0.0.32-1
- Update to 0.0.32

* Mon Oct 05 2015 Josef Stribny <jstribny@redhat.com> - 0.0.31-1
- Update to 0.0.31

* Mon Sep 14 2015 Josef Stribny <jstribny@redhat.com> - 0.0.30-5
- Drop the rest of libvirt deps, they should be pulled via ruby-libvirt

* Mon Sep 14 2015 Josef Stribny <jstribny@redhat.com> - 0.0.30-4
- Drop unnecessary explicit libvirt require

* Fri Jul 10 2015 Dan Williams <dcbw@redhat.com> - 0.0.30-3
- Fix: pass MAC addresses to vagrant to configure interfaces correctly

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.30-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 08 2015 Michael Adam <madam@redhat.com> - 0.0.30-1
- Update to 0.0.30 (#1220194)

* Tue Apr 21 2015 Josef Stribny <jstribny@redhat.com> - 0.0.26-2
- Fix: Wait for libvirt to shutdown the domain

* Mon Apr 20 2015 Josef Stribny <jstribny@redhat.com> - 0.0.26-1
- Update to 0.0.26

* Tue Mar 10 2015 Josef Stribny <jstribny@redhat.com> - 0.0.25-1
- Update to 0.0.25

* Wed Jan 28 2015 Michael Adam <madam@redhat.com> - 0.0.24-3
- Ship the polkit rules file as example in the docs package.

* Wed Jan 28 2015 Vít Ondruch <vondruch@redhat.com> - 0.0.24-2
- Do not ship polkit rules for now, since this might have security implications.

* Fri Jan 23 2015 Michael Adam <madam@redhat.com> - 0.0.24-2
- Move README.md to main package as doc.
- Rename 10-vagrant.rules to 10-vagrant-libvirt.rules.
- Move LICENSE to main package as license file.
- Remove shebang from non-executable Rakefile.

* Thu Jan 22 2015 Michael Adam <madam@redhat.com> - 0.0.24-1
- Update to version 0.0.24.

* Thu Jan 22 2015 Michael Adam <madam@redhat.com> - 0.0.23-4
- Fix rake dependency.
- Rename patch file.
- Improve description.

* Thu Nov 27 2014 Vít Ondruch <vondruch@redhat.com> - 0.0.23-4
- Add vagrant(vagrant-libvirt) virtual provide.

* Wed Nov 26 2014 Vít Ondruch <vondruch@redhat.com> - 0.0.23-3
- Enable test suite.
- Update polkit rules.

* Mon Nov 24 2014 Josef Stribny <jstribny@redhat.com> - 0.0.23-2
- Register and unregister the plugin using macros

* Tue Oct 14 2014 Josef Stribny <jstribny@redhat.com> - 0.0.23-1
- Update to 0.0.23
- Use ruby-libvirt 0.5.x
- Move the rest of the doc files to -doc

* Tue Sep 16 2014 Josef Stribny <jstribny@redhat.com> - 0.0.20-2
- Register and unregister automatically

* Wed Sep 10 2014 Josef Stribny <jstribny@redhat.com> - 0.0.20-1
- Update to 0.0.20

* Fri Jun 27 2014 Adam Miller <maxamillion@fedoraproject.org> - 0.0.16-1
- Initial package for Fedora
