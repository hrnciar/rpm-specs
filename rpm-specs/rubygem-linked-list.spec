# Generated from linked-list-0.0.13.gem by gem2rpm -*- rpm-spec -*-
%global gem_name linked-list

Name: rubygem-%{gem_name}
Version: 0.0.15
Release: 1%{?dist}
Summary: Ruby implementation of Doubly Linked List, following some Ruby idioms
License: MIT
URL: https://github.com/spectator/linked-list
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
# Needed for tests
BuildRequires: rubygem(minitest)
BuildArch: noarch

%description
Ruby implementation of Doubly Linked List, following some Ruby idioms.


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -n %{gem_name}-%{version}

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

find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x

%check
pushd .%{gem_instdir}

ruby -Ilib:test -e 'Dir.glob "./test/*_test.rb", &method(:require)'
popd

%files
%dir %{gem_instdir}
%exclude %{gem_instdir}/.*
%license %{gem_instdir}/LICENSE.txt
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/linked-list.gemspec
%{gem_instdir}/bin
%{gem_instdir}/test

%changelog
* Sun Aug 09 2020 Leigh Scott <leigh123linux@gmail.com> - 0.0.15-1
- Update to 0.0.15

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Dec 03 2019 Leigh Scott <leigh123linux@gmail.com> - 0.0.13-1
- Initial package
