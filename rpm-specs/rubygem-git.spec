# Generated from git-1.3.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name git

Name: rubygem-%{gem_name}
Version: 1.5.0
Release: 3%{?dist}
Summary: Ruby/Git is a Ruby library that can be used to create, read and manipulate Git repositories by wrapping system calls to the git binary
License: MIT
URL: http://github.com/schacon/ruby-git
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# One test fails inside mock but not otherwise
# ToDo understand why...
Patch0: disable-one-test.patch

# SOURCE1 contains the upstream tag of the project from github
# in particular this includes the spec directory which was not
# included in the gemfile.
Source1: https://github.com/ruby-git/ruby-git/archive/v%{version}/ruby-git-%{version}.tar.gz


BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby >= 1.9
BuildRequires: rubygem(test-unit)
BuildRequires: git-core
BuildArch: noarch
Requires:  git-core
%description
Ruby/Git is a Ruby library that can be used to create, read and manipulate Git
repositories by wrapping system calls to the git binary.


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -n %{gem_name}-%{version}

# unpack only the spec files from SOURCE1.
tar zxf %{SOURCE1} ruby-git-%{version}/tests --strip-components 1

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
# git fails fatally if it cannot guess as email adress
# as is the case inside mock.
git config --global user.email "you@example.com"
git config --global user.name "Your Name"
pushd tests
ruby ./all_tests.rb
popd

%files
%dir %{gem_instdir}
%license %{gem_instdir}/LICENSE
%{gem_instdir}/MAINTAINERS.md
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/CONTRIBUTING.md

%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Nov 15 2019 Steve Traylen <steve.traylen@cern.ch> - 1.5.0-2
- Install and run unit tests.

* Thu Nov 14 2019 Steve Traylen <steve.traylen@cern.ch> - 1.5.0-1
- Up to 1.5.0.

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed May 16 2018 Steve Traylen <steve.traylen@cern.ch> - 1.4.0-1
- Up to 1.4.0.

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Nov 03 2017 Steve Traylen <steve.traylen@cern.ch> - 1.3.0-1
- Regenerate modern spec file. 
- Add dependency on git-core rhbz#1489845
- Up to 1.3.0

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.5-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Mar 20 2013 Josef Stribny <jstribny@redhat.com> - 1.2.5-7
- Rebuild for https://fedoraproject.org/wiki/Features/Ruby_2.0.0

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Feb 02 2012 Vít Ondruch <vondruch@redhat.com> - 1.2.5-4
- Rebuilt for Ruby 1.9.3.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Dec 22 2009 Jeroen van Meeuwen <j.van.meeuwen@ogd.nl> - 1.2.5-1
- New upstream version

* Wed Oct 14 2009 Jeroen van Meeuwen <j.van.meeuwen@ogd.nl> - 1.2.4-1
- New upstream version

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Oct 02 2008 Jeroen van Meeuwen <kanarip@fedoraproject.org> - 1.0.7-4
- Fix %%doc

* Mon Sep 08 2008 Jeroen van Meeuwen <kanarip@fedoraproject.org> - 1.0.7-3
- Add ruby(abi) = 1.8 requires (#459883, tibbs)

* Sun Sep 07 2008 Jeroen van Meeuwen <kanarip@fedoraproject.org> - 1.0.7-2
- Fix up comments from review (#459883, JonRob)

* Sat Aug 23 2008 Jeroen van Meeuwen <kanarip@fedoraproject.org> - 1.0.7-1
- Initial package for review

