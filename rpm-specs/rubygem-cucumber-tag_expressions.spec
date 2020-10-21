# Generated from cucumber-tag_expressions-1.1.1.gem by gem2rpm -*- rpm-spec -*-
%global gem_name cucumber-tag_expressions

Name: rubygem-%{gem_name}
Version: 2.0.2
Release: 2%{?dist}
Summary: Cucumber tag expressions for ruby
License: MIT
URL: https://cucumber.io/docs/cucumber/api/#tag-expressions
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildRequires: %{_bindir}/rspec
BuildRequires: rubygem(rspec-expectations)
BuildArch: noarch

%description
Cucumber tag expressions for ruby.


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -n %{gem_name}-%{version}

sed -i -e 's|#!/usr/bin/env ruby|#!/usr/bin/ruby|' %{_builddir}/%{gem_name}-%{version}/bin/cucumber-tag-expressions

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


mkdir -p %{buildroot}%{_bindir}
cp -a .%{_bindir}/* \
        %{buildroot}%{_bindir}/

find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x

%check
pushd .%{gem_instdir}
rspec spec
popd

%files
%dir %{gem_instdir}
%{_bindir}/cucumber-tag-expressions
%license %{gem_instdir}/LICENSE
%{gem_instdir}/bin
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md
%{gem_instdir}/spec

%changelog
* Sat Aug 22 2020 jackorp <jar.prokop@volny.cz> - 2.0.2-2
- Fix homepage and shebang in bin/cucumber-tag-expressions.

* Sat Aug 22 01:14:34 GMT 2020 Pavel Valena <pvalena@redhat.com> - 2.0.2-1
- Update to cucumber-tag_expressions 2.0.2.
  Resolves: rhbz#1742043

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Aug 07 2018 jackorp <jar.prokop@volny.cz> - 1.1.1-1
- Initial package
