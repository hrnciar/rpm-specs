# Generated from vagrant-sshfs-1.1.0.gem by gem2rpm -*- rpm-spec -*-
%global vagrant_plugin_name vagrant-sshfs

Name: %{vagrant_plugin_name}
Version: 1.3.5
Release: 2%{?dist}
Summary: A Vagrant synced folder plugin that mounts folders via SSHFS
License: GPLv2
URL: https://github.com/dustymabe/vagrant-sshfs
Source0: https://github.com/dustymabe/vagrant-sshfs/archive/v%{version}.tar.gz

Requires: vagrant >= 1.9.1
BuildRequires: vagrant >= 1.9.1
BuildRequires: rubygems
BuildRequires: rubygem(rdoc)
BuildArch: noarch
Provides: vagrant(%{vagrant_plugin_name}) = %{version}

%description
A Vagrant synced folder plugin that mounts folders via SSHFS. 
This is the successor to Fabio Kreusch's implementation:
https://github.com/fabiokr/vagrant-sshfs.


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -T -b 0 -q -n %{vagrant_plugin_name}-%{version}

# since we don't have the full git repo we can't use `git ls-files`
sed -i 's/git ls-files -z/find . -type f -print0/' %{vagrant_plugin_name}.gemspec

# remove dependencies on windows libraries (needed for windows, not linux)
sed -i '/win32-process/d' %{vagrant_plugin_name}.gemspec

%build
# Create the gem as gem install only works on a gem file
gem build %{vagrant_plugin_name}.gemspec

# %%vagrant_plugin_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%vagrant_plugin_install

%install
mkdir -p %{buildroot}%{vagrant_plugin_dir}
cp -a .%{vagrant_plugin_dir}/* \
        %{buildroot}%{vagrant_plugin_dir}/



%files
%dir %{vagrant_plugin_instdir}
%license %{vagrant_plugin_instdir}/LICENSE
%{vagrant_plugin_libdir}
%{vagrant_plugin_instdir}/locales
%exclude %{vagrant_plugin_cache}
%{vagrant_plugin_spec}
# Ingore some files that probbaly shouldn't be in the gem
%exclude %{vagrant_plugin_instdir}/.gitignore
%exclude %{vagrant_plugin_instdir}/test
%exclude %{vagrant_plugin_instdir}/features
%exclude %{vagrant_plugin_instdir}/build.sh

%files doc
%license %{vagrant_plugin_instdir}/LICENSE
%doc %{vagrant_plugin_docdir}
%{vagrant_plugin_instdir}/Gemfile
%doc %{vagrant_plugin_instdir}/README.adoc
%doc %{vagrant_plugin_instdir}/RELEASE.txt
%{vagrant_plugin_instdir}/Rakefile
%{vagrant_plugin_instdir}/vagrant-sshfs.gemspec

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun 29 2020 Dusty Mabe <dusty@dustymabe.com> - 1.3.5-1
- new upstream release: 1.3.5

* Mon Mar 16 2020 Dusty Mabe <dusty@dustymabe.com> - 1.3.4-1
- new upstream release: 1.3.4

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Jan 05 2020 Dusty Mabe <dusty@dustymabe.com> - 1.3.3-1
- new upstream release: 1.3.3

* Wed Dec 11 2019 Dusty Mabe <dusty@dustymabe.com> - 1.3.2-1
- new upstream release: 1.3.2

* Tue Dec 10 2019 Dusty Mabe <dusty@dustymabe.com> - 1.3.1-5
- Change to build from tar archive. Preparing for packit.

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Mar 12 2018 Dusty Mabe <dusty@dustymabe.com> - 1.3.1-1
- New version of sshfs: 1.3.1

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Feb 14 2017 Vít Ondruch <vondruch@redhat.com> - 1.3.0-3
- Drop registration macros for Vagrant 1.9.1 compatibility.

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Nov 26 2016 Dusty Mabe <dusty@dustymabe.com> - 1.3.0-1
- New version of sshfs: 1.3.0

* Fri Nov 11 2016 Dusty Mabe <dusty@dustymabe.com> - 1.2.1-2
- Use release '2' because I messed up the last changelog entry.

* Fri Nov 11 2016 Dusty Mabe <dusty@dustymabe.com> - 1.2.1-1
- New version of sshfs out: 1.2.1

* Tue Aug 30 2016 Dusty Mabe <dusty@dustymabe.com> - 1.2.0-2
- Bump release to 2 because vagrant-sshfs-1.2.0-1.fc2{2,3,4} is what
  is available from copr. Bumping to 2 will make sure we don't
  have any confusion.

* Tue Aug 30 2016 Dusty Mabe <dusty@dustymabe.com> - 1.2.0-1
- Remove unnecessary provides of bundled fonts
- Update to 1.2.0 release
- Add patch to remove requirement of win32-process rubygem

* Wed Mar 30 2016 Dusty Mabe <dusty@dustymabe.com> - 1.1.0-1
- Initial package for Fedora
