%global gem_name jekyll-sass-converter

Name:           rubygem-%{gem_name}
Version:        2.1.0
Release:        2%{?dist}
Summary:        Basic Sass converter for Jekyll
License:        MIT

URL:            https://github.com/jekyll/jekyll-sass-converter
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
Source1:        %{url}/archive/v%{version}/%{gem_name}-%{version}.tar.gz

# disable one slightly broken test depending on exact error message content
Patch0:         00-disable-broken-test.patch

BuildRequires:  ruby(release)
BuildRequires:  rubygems-devel
BuildRequires:  ruby

BuildRequires:  rubygem(jekyll) >= 4.0.0
BuildRequires:  rubygem(minima)
BuildRequires:  rubygem(rspec)

BuildArch:      noarch

%description
A basic Sass converter for Jekyll.


%package        doc
Summary:        Documentation for %{name}
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch

%description    doc
Documentation for %{name}.


%prep
%setup -q -n %{gem_name}-%{version}

# extract README, LICENSE, and test files not shipped with the gem
mkdir upstream && pushd upstream
tar -xzvf %{SOURCE1}
mv %{gem_name}-%{version}/spec ../spec
mv %{gem_name}-%{version}/README.md ../
mv %{gem_name}-%{version}/LICENSE.txt ../
popd && rm -r upstream

%patch0 -p1



%build
gem build ../%{gem_name}-%{version}.gemspec

%gem_install


%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* %{buildroot}%{gem_dir}/


%check
rspec spec


%files
%license LICENSE.txt
%doc README.md

%dir %{gem_instdir}

%{gem_libdir}

%exclude %{gem_cache}

%{gem_spec}

%files doc
%doc %{gem_docdir}


%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Feb 06 2020 Fabio Valentini <decathorpe@gmail.com> - 2.1.0-1
- Update to version 2.1.0.

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Sep 28 2019 Fabio Valentini <decathorpe@gmail.com> - 2.0.1-1
- Update to version 2.0.1.

* Fri Sep 13 2019 Fabio Valentini <decathorpe@gmail.com> - 2.0.0-1
- Update to version 2.0.0.

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 01 2018 Fabio Valentini <decathorpe@gmail.com> - 1.5.2-1
- Update to version 1.5.2.

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Apr 09 2017 Björn Esser <besser82@fedoraproject.org> - 1.5.0-1
- Update to 1.5.0 (rhbz#1395000)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Aug 23 2016 Björn Esser <fedora@besser82.io> - 1.4.0-1
- initial import (#1368846)

* Sun Aug 21 2016 Björn Esser <fedora@besser82.io> - 1.4.0-0.1
- initial rpm-release (#1368846)

