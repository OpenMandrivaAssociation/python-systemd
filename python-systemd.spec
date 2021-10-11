# Work around incomplete debug packages
%global _empty_manifest_terminate_build 0

Summary:	Python interface to systemd
Name:		python-systemd
Version:	234
Release:	6
Group:		System/Kernel and hardware
License:	LGPLv2+
Url:		https://github.com/systemd/python-systemd
Source0:	https://github.com/systemd/python-systemd/archive/%{name}-%{version}.tar.gz
BuildRequires:	pkgconfig(python)
BuildRequires:	pkgconfig(libsystemd)

%description
Provides Python scripting interface to systemd.

%prep
%autosetup -p1

%build
%set_build_flags
export CFLAGS="%{optflags} -lpython%{python_version}"
%py_build

%install
%py_install

%files
%doc README.md LICENSE.txt NEWS
%dir %{py_platsitedir}/systemd
%{py_platsitedir}/systemd/test/*.py
%{py_platsitedir}/systemd/*.py
%{py_platsitedir}/systemd/*.so
%{py_platsitedir}/*.egg-info
