# Generated from notiffany-0.1.1.gem by gem2rpm -*- rpm-spec -*-
%global gem_name notiffany

Name: rubygem-%{gem_name}
Version: 0.1.3
Release: 2%{?dist}
Summary: Notifier library (extracted from Guard project)
License: MIT
URL: https://github.com/guard/notiffany
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# git clone https://github.com/guard/notiffany.git && cd notiffany
# git checkout v0.1.3
# tar -czvf rubygem-notiffany-0.1.3-spec.tar.gz spec/
Source1: rubygem-notiffany-0.1.3-spec.tar.gz
# Fix "uninitialized constant Notiffany::VERSION" test failure
# https://github.com/guard/notiffany/pull/31
Patch0: rubygem-notiffany-0.1.1-Fix-uninitialized-constant-Notiffany-VERSION-test-failure.patch
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildRequires: rubygem(rspec)
BuildRequires: rubygem(nenv)
BuildRequires: rubygem(shellany)
BuildArch: noarch

%description
Wrapper libray for most popular notification
libraries such as Growl, Libnotify, Notifu.


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -n %{gem_name}-%{version} -b 1

pushd %{_builddir}
%patch0 -p1
popd

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
ln -s %{_builddir}/spec spec
rspec spec
popd

%files
%dir %{gem_instdir}
%license %{gem_instdir}/LICENSE.txt
%{gem_instdir}/images
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md

%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Aug 18 2019 Jaroslav Prokop <jar.prokop@volny.cz> - 0.1.3-1
- Update to Notiffany 0.1.3.

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Oct 25 2017 Jaroslav Prokop <jar.prokop@volny.cz> - 0.1.1-1
- Initial package
