%global gem_name kramdown-syntax-coderay

Name:           rubygem-%{gem_name}
Summary:        Coderay syntax highlighting for kramdown
Version:        1.0.1
Release:        3%{?dist}
License:        MIT

URL:            https://github.com/kramdown/syntax-coderay
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem

BuildArch:      noarch

BuildRequires:  ruby(release)
BuildRequires:  rubygems-devel
BuildRequires:  ruby >= 2.3

BuildRequires:  rubygem(coderay)
BuildRequires:  rubygem(kramdown) >= 2.0.0
BuildRequires:  rubygem(minitest)

%description
kramdown-syntax-coderay uses coderay to highlight code blocks/spans.


%package        doc
Summary:        Documentation for %{name}
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch

%description    doc
Documentation for %{name}.


%prep
%setup -q -n %{gem_name}-%{version}


%build
gem build ../%{gem_name}-%{version}.gemspec

%gem_install


%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* %{buildroot}%{gem_dir}/


%check
pushd .%{gem_instdir}
ruby -I'lib' -e 'Dir.glob "./test/test_*.rb", &method(:require)'
popd


%files
%license %{gem_instdir}/COPYING

%dir %{gem_instdir}
%{gem_instdir}/VERSION

%{gem_libdir}

%{gem_spec}

%exclude %{gem_cache}

%files doc
%doc %{gem_docdir}

%doc %{gem_instdir}/CONTRIBUTERS

%{gem_instdir}/test/


%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Aug 29 2019 Fabio Valentini <decathorpe@gmail.com> - 1.0.1-1
- Initial package

