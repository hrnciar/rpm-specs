# Generated from spring-watcher-listen-2.0.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name spring-watcher-listen

Name: rubygem-%{gem_name}
Version: 2.0.1
Release: 9%{?dist}
Summary: Makes spring watch files using the listen gem
License: MIT
URL: https://github.com/jonleighton/spring-watcher-listen
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# Fix Ruby 2.5 compatibility.
# https://github.com/jonleighton/spring-watcher-listen/pull/22
Patch0: rubygem-spring-watcher-listen-2.0.1-Really-delete-the-directories.patch
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildRequires: rubygem(spring)
BuildRequires: rubygem(listen)
BuildRequires: rubygem(activesupport)
# spring requires bundler as a runtime dependency.
BuildRequires: rubygem(bundler)

BuildArch: noarch

%description
This gem makes Spring watch the filesystem for changes using Listen rather than
by polling the filesystem. On larger projects this means spring will be more
responsive, more accurate and use less cpu on local filesystems.


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
gem unpack %{SOURCE0}

%setup -q -D -T -n  %{gem_name}-%{version}

gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec

%patch0 -p1

%build
# Create the gem as gem install only works on a gem file
gem build %{gem_name}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

# Run the test suite
%check
pushd .%{gem_instdir}
sed -i '/bundler\/setup/ s/^/#/' test/helper.rb
# Run only unit test now, acceptance test wants to compile gems extensions
mv test/acceptance_test.rb{,.disable}
# Asking about tests finish with a error "undefined method callback!".
# https://github.com/jonleighton/spring-watcher-listen/issues/12
ruby -Ilib:test -e 'Dir.glob "./test/**/*_test.rb", &method(:require)'
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
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/spring-watcher-listen.gemspec
%{gem_instdir}/test

%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 17 2018 Vít Ondruch <vondruch@redhat.com> - 2.0.1-4
- Fix Ruby 2.5 compatibility.

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Dec 15 2016 Jun Aruga <jaruga@redhat.com> - 2.0.1-1
- Update to 2.0.1

* Thu Jul 28 2016 Jun Aruga <jaruga@redhat.com> - 2.0.0-1
- Initial package
