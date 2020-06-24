%global gem_name sassc
%define debug_package %{nil}

Name:           rubygem-%{gem_name}
Summary:        Use libsass with Ruby!
Version:        2.4.0
Release:        1%{?dist}
License:        MIT

URL:            https://github.com/sass/sassc-ruby
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem

# disable tests that are broken because of the unbundled libsass
Patch0:         00-disable-broken-tests.patch

BuildRequires:  ruby-devel >= 2.0.0
BuildRequires:  rubygems-devel
BuildRequires:  ruby(release)

# test requirements
BuildRequires:  libsass
BuildRequires:  rubygem(ffi)
BuildRequires:  rubygem(minitest)
BuildRequires:  rubygem(minitest-around)
BuildRequires:  rubygem(pry)
BuildRequires:  rubygem(test_construct)

Requires:       libsass

%description
Use libsass with Ruby!


%package        doc
Summary:        Documentation for %{name}
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch

%description    doc
Documentation for %{name}.


%prep
%autosetup -n %{gem_name}-%{version} -p1

# disable building bundled libsass
sed -i "/s\.extensions/d" ../%{gem_name}-%{version}.gemspec


%build
# use libsass.so.1 from host
sed -i "s/libsass\.\#{dl_ext}/libsass\.\#{dl_ext}\.1/" lib/sassc/native.rb
sed -i "s!__dir__!\"%{_libdir}\"!" lib/sassc/native.rb

gem build ../%{gem_name}-%{version}.gemspec

%gem_install


%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* %{buildroot}%{gem_dir}/


%check
pushd .%{gem_instdir}
ruby -Ilib -e 'Dir.glob "./test/**_test.rb", &method(:require)'
popd


%files
%license %{gem_instdir}/LICENSE.txt

%{gem_libdir}
%{gem_spec}

%dir %{gem_instdir}

%exclude %{gem_instdir}/ext/
%exclude %{gem_instdir}/sassc.gemspec
%exclude %{gem_instdir}/.gitignore
%exclude %{gem_instdir}/.gitmodules
%exclude %{gem_instdir}/.travis.yml

%exclude %{gem_cache}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/CODE_OF_CONDUCT.md
%doc %{gem_instdir}/README.md

%{gem_instdir}/Gemfile
%{gem_instdir}/Rakefile
%{gem_instdir}/test/


%changelog
* Sat Jun 06 2020 Fabio Valentini <decathorpe@gmail.com> - 2.4.0-1
- Update to version 2.4.0.

* Sat Apr 18 2020 Fabio Valentini <decathorpe@gmail.com> - 2.3.0-1
- Update to version 2.3.0.

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Aug 28 2019 Fabio Valentini <decathorpe@gmail.com> - 2.2.0-1
- Update to version 2.2.0.

* Tue Aug 20 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.0-1
- Initial package

