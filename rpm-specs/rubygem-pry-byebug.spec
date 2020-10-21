# Generated from pry-byebug-3.6.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name pry-byebug

Name: rubygem-%{gem_name}
Version: 3.6.0
Release: 7%{?dist}
Summary: Fast debugging with Pry
License: MIT
URL: https://github.com/deivid-rodriguez/pry-byebug
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby >= 2.2.0
BuildArch: noarch

%description
Combine 'pry' with 'byebug'. Adds 'step', 'next', 'finish',
'continue' and 'break' commands to control execution.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%autosetup -n  %{gem_name}-%{version}

%build
# https://github.com/deivid-rodriguez/pry-byebug/commit/036f94c67bb3eff36cda54400d9833062d9002dc
# Allow byebug 11.0 and above
sed -i ../%{gem_name}-%{version}.gemspec \
	-e '\@byebug@s|10\.0|11.0|' \
	%{nil}

gem build ../%{gem_name}-%{version}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%files
%dir %{gem_instdir}
%license %{gem_instdir}/LICENSE
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/README.md

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Feb 19 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.6.0-4
- Allow byebug 11.0 and above

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Sep 14 2018 Steve Traylen <steve.traylen@cern.ch> - 3.6.0-2
- Use %%autosetup

* Wed Sep 12 2018 Steve Traylen <steve.traylen@cern.ch> - 3.6.0-1
- Initial package
