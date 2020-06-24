# Generated from jekyll-git-authors-0.2.1.gem by gem2rpm -*- rpm-spec -*-
%global gem_name jekyll-git-authors

Name: rubygem-%{gem_name}
Version: 1.0.0
Release: 3%{?dist}
Summary: Jekyll plugin that adds git authors into your page
License: MIT
URL: https://gitlab.com/jackorp/jekyll-git-authors
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: %{_bindir}/git
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildRequires: %{_bindir}/git
BuildRequires: rubygem(jekyll)
BuildRequires: rubygem(minitest)
BuildRequires: rubygem(cucumber) >= 3
BuildRequires: rubygem(rspec-expectations)
BuildArch: noarch

%description
Jekyll plugin that adds git authors and their obfuscated email address into
page using markdown and liquid.


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



%check
pushd .%{gem_instdir}

ruby -e 'Dir.glob "./test/**/*_test.rb", &method(:require)'
cucumber

popd

%files
%dir %{gem_instdir}
%license %{gem_instdir}/LICENSE.txt
%{gem_libdir}
%{gem_spec}
%exclude %{gem_cache}
%exclude %{gem_instdir}/.*

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md
%doc %{gem_instdir}/jekyll-git-authors.gemspec
%{gem_instdir}/Gemfile
%{gem_instdir}/Rakefile
%{gem_instdir}/features
%{gem_instdir}/test

%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Feb 12 2019 Jaroslav Prokop <jar.prokop@volny.cz> - 1.0.0-1
- Update to 1.0.0 release.

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Jul 29 2018 jackorp <jar.prokop@volny.cz> - 0.2.1-1
- Initial package
