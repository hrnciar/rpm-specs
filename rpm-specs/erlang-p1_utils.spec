%global srcname p1_utils


Name:       erlang-%{srcname}
Version:    1.0.17
Release:    1%{?dist}
BuildArch:  noarch

License:    ASL 2.0
Summary:    Erlang utility modules from ProcessOne
URL:        https://github.com/processone/p1_utils/
Source0:    https://github.com/processone/p1_utils/archive/%{version}/p1_utils-%{version}.tar.gz
Patch1:     erlang-p1_utils-0001-Don-t-use-function-from-Ejabberd.patch

BuildRequires: erlang-rebar


%description
p1_utils is an application containing ProcessOne modules and tools that are
leveraged in other development projects.


%prep
%autosetup -p1 -n %{srcname}-%{version}
# This file was 755 upstream, which causes an rpmlint warning. This pull request has
# been created to fix the issue upstream:
# https://github.com/processone/p1_utils/pull/4
chmod 0644 doc/style.css

# https://github.com/processone/p1_utils/pull/7
sed -i "/.*Created.*/d" src/p1_options.erl


%build
%{rebar_compile}
%{rebar_doc}


%check
%{rebar_eunit}


%install
%{erlang_install}


%files
%license LICENSE.txt
%doc CHANGELOG.md
%doc doc
%doc README.md
%{erlang_appdir}


%changelog
* Fri Feb 14 2020 Randy Barlow <bowlofeggs@fedoraproject.org> - 1.0.17-1
- Update to 1.0.17 (#1788909).
- https://github.com/processone/p1_utils/blob/1.0.17/CHANGELOG.md

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Sep 03 2019 Randy Barlow <bowlofeggs@fedoraproject.org> - 1.0.16-1
- Update to 1.0.16 (#1742472).
- https://github.com/processone/p1_utils/blob/1.0.16/CHANGELOG.md

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jun 05 2019 Randy Barlow <bowlofeggs@fedoraproject.org> - 1.0.15-1
- Update to 1.0.15 (#1713425).
- https://github.com/processone/p1_utils/blob/1.0.15/CHANGELOG.md

* Sat Apr 13 2019 Randy Barlow <bowlofeggs@fedoraproject.org> - 1.0.14-1
- Update to 1.0.14 (#1683182).
- https://github.com/processone/p1_utils/blob/1.0.14/CHANGELOG.md

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild
