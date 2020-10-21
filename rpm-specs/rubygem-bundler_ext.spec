# Generated from bundler_ext-0.1.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name bundler_ext

Summary: Load system gems via Bundler DSL
Name: rubygem-%{gem_name}
Version: 0.4.1
Release: 11%{?dist}
License: MIT
URL: https://github.com/bundlerext/bundler_ext
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
# Fix test failures due to Bundler 1.8.1+.
# https://github.com/bundlerext/bundler_ext/pull/22
Patch0: rubygem-bundler_ext-0.4.1-Fix-Bundler-1.8.1-test-failures.patch
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildRequires: rubygem(rspec) < 3
BuildRequires: rubygem(bundler)
BuildRequires: rubygem(rails)
BuildArch: noarch

%description
Simple library leveraging the Bundler Gemfile DSL to load gems already on the
system and managed by the systems package manager (like yum/apt)


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
rspec2 spec
popd

%files
%dir %{gem_instdir}
%exclude %{gem_instdir}/.*
%license %{gem_instdir}/MIT-LICENSE
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/spec

%changelog
* Wed Sep 16 2020 Vít Ondruch <vondruch@redhat.com> - 0.4.1-1
- Fix FTBFS due to test failures with Bundler 1.8.1+.
  Resolves: rhbz#1865408

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-10
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu May 26 2016 Jun Aruga <jaruga@redhat.com> - 0.4.1-1
- Update to bundler_ext 0.4.1. (rhbz#1332928)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Mar 02 2015 Vít Ondruch <vondruch@redhat.com> - 0.4.0-1
- Update to bundler_ext 0.4.0.

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Jul 30 2013 Vít Ondruch <vondruch@redhat.com> - 0.3.1-1
- Update to bundler_ext 0.3.1.

* Thu Jul 18 2013 Vít Ondruch <vondruch@redhat.com> - 0.3.0-1
- Update to bundler_ext 0.3.0.

* Wed Nov 28 2012 Vít Ondruch <vondruch@redhat.com> - 0.1.0-4
- Yet again RHEL6 and Fedora 16 compatibility fixes.

* Fri Nov 23 2012 Vít Ondruch <vondruch@redhat.com> - 0.1.0-3
- More RHEL6 and Fedora 16 compatibility.

* Thu Nov 22 2012 Vít Ondruch <vondruch@redhat.com> - 0.1.0-2
- Add RHEL6 and Fedora 16 compatibility. 

* Tue Nov 20 2012 Vít Ondruch <vondruch@redhat.com> - 0.1.0-1
- Initial package
